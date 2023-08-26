<script>
  import { invoke } from '@tauri-apps/api/tauri'
  let json_text = '';
  let obj = '';
  let sites='';

  async function get_sites() {
    json_text = await invoke('get_sites', {});
    obj=JSON.parse(json_text);
    sites=obj.sites;
  }
  get_sites()

  function test_fn(){
    console.log("Conosle test");
  }

  const navButton = document.getElementById('nav-button');

</script>
  <style>
  #debug{
    background-color: white;
  }
</style>
  <input value="AAAAAAAAAAAAAAAAA" type="button" onClick="test_fn()" />
  <nav class="navbar">
    <ul class="navbar-nav">
      <li class="logo">
        <button id="nav_button" class="main_button">
	        <img class="icono" src="logo.png" alt="Menu">
        </button>
      </li>
	{#each sites as site}
	      <li class="nav-item">
	        <button class="nav-link" >
			      <div class="site-icon">
              {@html site.svg}
            </div>
		        <span class="link-text" id = {site.file}>{site.name}</span>
	        </button>
	      </li>
	{/each}

      <li class="nav-item">
        <button id="nav_button" class="main_button">
	        <img class="icono" src="img.png" alt="Menu">
        </button>
      </li>
    </ul>
  </nav>


