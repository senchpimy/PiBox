use std::fs;
use serde::{Deserialize, Serialize};
use serde_json::Result;


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

#[tauri::command]
fn get_sites(name:&str)->String{
    let site = Site {
        file:"TEST".to_string(),
        name:"NAME".to_string(),
        svg:"SVG".to_string()
    };
    println!("Hola");
    let paths = fs::read_dir("./").unwrap();
    for p in paths{
        print!("Name:{};",p.unwrap().path().display());
    }
    let j = serde_json::to_string(&site).unwrap();
    j
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .invoke_handler(tauri::generate_handler![get_sites])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
