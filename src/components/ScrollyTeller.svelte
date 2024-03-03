<script>
  import Scroller from '@sveltejs/svelte-scroller';
  import { base } from '$app/paths';
  import F1 from './F1.svelte'
  import Text from './Text.svelte'
  import Map from './Map.svelte'
  import Graph from './Graph.svelte'
  import { onMount } from 'svelte';

  let count, index, offset, progress;
  let width, height;

  onMount(() => {
    const style = document.createElement('style');
    style.textContent = `
      @font-face {
        font-family: 'Formula1-Bold';
        src: url('${base}/Formula1-Bold.otf') format('opentype');
      }
    `;
    document.head.appendChild(style);
  });
</script>

<style>
  section {
    height: 80vh;
    background-color: rgba(0, 0, 0, 0); /* 20% opaque */
    /* color: white; */
    outline: magenta solid 3px;
    text-align: center;
    max-width: 1400px; /* adjust at will */
    color: black;
    padding: 1em;
    margin: 0 0 2em 0;
  }
  .background {
    width: 100%;
    height: 100vh;
    position: relative;
    outline: green solid 3px;
  }

  .foreground {
    width: 80%;
    margin: auto;
    height: auto;
    position: relative;
    outline: red solid 3px;
  }
  .progress-bars {
    position: absolute;
    background: rgba(170, 51, 120, 0.2);
    visibility: visible;
  }

  @font-face {
    font-family: 'Formula1-Regular';
     src: url('Formula1-Regular.otf') format('opentype');
  }

  @font-face {
    font-family: 'Formula1-Wide';
    src: url('Formula1-Wide.otf') format('opentype');
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
    <Map {index}/>
    <F1 {index}/>
    <Text {index}/>

    <div class='progress-bars'>
      <p>current section: <strong>{index + 1}/{count}</strong></p>
      <progress value={count ? (index + 1) / count : 0} />

      <p>offset in current section</p>
      <progress value={offset || 0} />

      <p>total progress</p>
      <progress value={progress || 0} />
    </div>
  </div>

  <div class='foreground' slot='foreground'>
    <section></section>
    <section></section>
    <section>This is the third section.</section>
    <section>This is the fourth section.</section>
    <section></section>
  </div>
</Scroller>

