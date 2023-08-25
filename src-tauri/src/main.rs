use std::fs;
use pyo3::prelude::*;
use pyo3::types::PyTuple;
use serde::{Deserialize, Serialize};
//use serde_json::Result;


#[tauri::command]
fn greet(name: &str) -> String {
    println!("HOLA");
    let paths = fs::read_dir("../sites").unwrap();
    for p in paths{
        println!("Name:{};",p.unwrap().path().display());
    }
    println!("HOLA");
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[derive(Serialize, Deserialize)]
struct Site{
    file:String,
    name:String,
    svg:String,
}

#[derive(Serialize, Deserialize,Default)]
struct Sites{
    sites:Vec<Site>,
}

#[tauri::command]
fn get_sites()->String{
    let paths = fs::read_dir("../sites/").unwrap();
    let mut sites = Sites::default(); 
    pyo3::prepare_freethreaded_python();
    for p in paths{
        //let mut  name:&str;
        let pp = p.unwrap();
        let p = pp.path().clone();
        println!("Name:{};",p.display());
        let contents = fs::read_to_string(pp.path())
            .expect("Should have been able to read the file");
        println!("{}",contents);
        let name:String = Python::with_gil(|py| {
             let fun: Py<PyAny> = PyModule::from_code(
                 py,
                &contents,
                 "",
                 "",
             ).unwrap()
             .getattr("name").unwrap()
             .into();

            let result = fun.call0(py).unwrap();
            let e=result.extract::<&str>(py).unwrap();
            e.to_string()
        });
        let s = Site{
            file:"AÑAÑAÑ".to_string(),
            name:pp.path().clone().to_str().unwrap().to_string(),
            svg:name
        };
        sites.sites.push(s);
    }
    let j = serde_json::to_string(&sites).unwrap();
    println!("{}",j);
    j
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .invoke_handler(tauri::generate_handler![get_sites])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
