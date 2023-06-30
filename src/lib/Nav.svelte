<script>
  import { invoke } from '@tauri-apps/api/tauri'
  let json_text = ''
  let name = ''
  let obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');

  async function get() {
    json_text = await invoke('get_sites', { name })
    obj=JSON.parse(json_text)
  }
   get()
  const sections = {
		"Title 1": "paragraph",
		"Title 3": "paragraph",
	}
  const navButton = document.getElementById('nav-button');
</script>
  <nav class="navbar">
    <ul class="navbar-nav">
      <li class="logo">
        <button id="nav_button" class="main_button">
	        <img class="icono" src="logo.png" alt="Menu">
        </button>
      </li>
      <h1>{obj.name}</h1>

	{#each Object.entries(sections) as [title, paragraph]}
	      <li class="nav-item">
	        <a href="#" class="nav-link">
			<img class="icono" src="img.png" alt="{paragraph}">
		<span class="link-text">{title}</span>
	        </a>
	      </li>
	{/each}

      <li class="nav-item">
        <button id="nav_button" class="main_button">
	<img class="icono" src="img.png" alt="Menu">
        </button>
      </li>
    </ul>
  </nav>


