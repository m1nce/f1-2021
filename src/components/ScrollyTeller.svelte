<script>
  import Scroller from '@sveltejs/svelte-scroller';
  import Map from './Map.svelte'
  import Graph from './Graph.svelte'

  let count, index, offset, progress;
  let width, height;
</script>

<main>
  <h1>Abu Dhabi 2021</h1>
</main>

<style>
  .background {
    width: 100%;
    height: 100vh;
    position: relative;
    outline: green solid 3px;
  }

  .progress-bars {
    position: absolute;
    background: rgba(170, 51, 120, 0.2);
    visibility: visible;
  }

</style>

<Scroller 
  top={0.0}
  bottom={1}
  threshold={0.5}
  bind:count
  bind:index
  bind:offset
  bind:progress
>

  <div
    class='background'
    slot='background'
    bind:clientWidth={width}
    bind:clientHeight={height}
  >
    <div class='progress-bars'>
      <p>current section: <strong>{index + 1}/{count}</strong></p>
      <progress value={count ? (index + 1) / count : 0} />

      <p>offset in current section</p>
      <progress value={offset || 0} />

      <p>total progress</p>
      <progress value={progress || 0} />
    </div>
  </div>

</Scroller>

