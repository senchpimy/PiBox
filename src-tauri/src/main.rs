use std::fs;

#[tauri::command]
fn greet(name: &str) -> String {
    println!("HOLA");
    let paths = fs::read_dir("../sites").unwrap();
    for p in paths{
        print!("Name:{};",p.unwrap().path().display());
    }
    format!("Hello, {}! You've been greeted from Rust!", name)
}

#[tauri::command]
fn get_sites(name:&str)->String{
    println!("Hola");
    let paths = fs::read_dir("./").unwrap();
    for p in paths{
        print!("Name:{};",p.unwrap().path().display());
    }
    "HOLA".to_string()
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![greet])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
