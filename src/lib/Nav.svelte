<script>
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
	<img class="icono" src="img.png" alt="Menu">
          <span class="link-text logo-text">Fireship</span>
        </button>
      </li>

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
          <span class="link-text logo-text">Fireship</span>
        </button>
      </li>
    </ul>
  </nav>


