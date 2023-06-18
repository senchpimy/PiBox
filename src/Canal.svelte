<script>
const data = {
"Video1" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video2" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video3" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video4" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video41" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video42" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video43" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video44" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video45" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video46" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video47" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video48" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video49" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video40" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video411" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video412" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video413" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video414" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video415" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video416" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video417" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video418" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video419" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video410" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video4111" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
"Video5" : {"Duracion":23,"img":"img.png", "url": "hhhhhhh"},
}
const c = {
"Id":"sdghfkghs",
"name":"Juanito",
"avatar":"img.png",
"info":"60 mil subs"
}
</script>

<link rel='stylesheet' href='/canal.css'>
<div class="fondo">
</div>

<div class="info">
  <img class="avatar" src="{c.avatar}" alt="">
  <div class="info_container">
  <h1 class="name">{c.name}</h1>
  <h2>{c.info}</h2>
  </div>
</div>
<div class="videos_container">
{#each Object.entries(data) as [title, conte]}
<button class="video">
    <div class="video_container">
      <img class="video_prev" src="{conte.img}">
    </div>
    <div class="duracion">
      <p>{conte.Duracion}</p>
    </div>
    <div class="descripcion">
      <p>{title}</p>
    </div>
</button>
{/each}
  
</div>
  
