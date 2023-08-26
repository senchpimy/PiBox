<script>
  import { invoke } from '@tauri-apps/api/tauri'
  let json_text = '';
  let obj = '';
  let sites='';

  async function get() {
    json_text = await invoke('get_sites', {});
    obj=JSON.parse(json_text);
    sites=obj.sites;
  }
  get()

  const navButton = document.getElementById('nav-button');

</script>
  <style>
  #debug{
    background-color: white;
  }
</style>
  <nav class="navbar">
    <ul class="navbar-nav">
      <li class="logo">
        <button id="nav_button" class="main_button">
	        <img class="icono" src="logo.png" alt="Menu">
        </button>
      </li>
	{#each sites as site}
	      <li class="nav-item">
	        <a href="#" class="nav-link">
			    <div class="icono">
            {@html site.svg}
          </div>
		<span class="link-text" id = {site.file}>{site.name}</span>
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


