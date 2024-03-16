<script>
  // Essential imports
  import Scroller from '@sveltejs/svelte-scroller';
  import { base } from '$app/paths';
  import { onMount } from 'svelte';

  // Building blocks of ScrollyTeller
  import F1 from './F1.svelte'
  import TextBase from './TextBase.svelte'
  import Map from './Map.svelte'
  import Pitstop from './Pitstop.svelte'
  import SergioTime from './SergioTime.svelte'
  import Hamovertake from './Hamovertake.svelte'
  import LafCrash from './LafCrash.svelte'
  import Lastlap from './Lastlap.svelte';
  import Graph from './Graph.svelte'

  // Initialize variables for ScrollyTeller
  let count, index, offset, progress;
  let width, height;
  index = 0;

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

  $: isYellowBackground = index > 21 && index <= 29;
</script>

<style>
  section {
    height: 80vh;
    background-color: rgba(0, 0, 0, 0); /* 20% opaque */
    /* color: white; */
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
    background-color: rgba(0, 0, 0, 0);
    transition: background-color 1s ease;
    z-index: -10;
  }

  .yellow-background {
    background-color: #FFFB98;
  }

  .foreground {
    width: 80%;
    margin: auto;
    height: auto;
    position: relative;
    z-index: -10;
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
>
  <div
    class='background {isYellowBackground ? 'yellow-background' : ''}'
    slot='background'
    bind:clientWidth={width}
    bind:clientHeight={height}
  >
    <Map {index}/>
    <Pitstop {index}/>
    <SergioTime {index}/>
    <Hamovertake {index}/>
    <LafCrash {index}/>
    <F1 {index}/>
    <TextBase {index}/>
    <Lastlap {index}/>
    <!-- <Graph {index}/> -->

  </div>

  <div class='foreground' slot='foreground'>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
    <section></section>
  </div>
</Scroller>