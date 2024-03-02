<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    import { fade } from 'svelte/transition';
    export let index;
    let isVisible = false;
    let LogoisVisible = true;
    let zoomLevel;
  
    onMount(() => {
      function updateZoomLevel() {
        const screenWidth = window.innerWidth;
        zoomLevel = screenWidth <= 600 ? 4 : 5.85; // Adjust values as needed
      }
  
      function handleResize() {
        updateZoomLevel();
        // Assuming 'map' is defined and used within your component
        // You need to initialize and define 'map' properly for your use case
        // map.setZoom(zoomLevel);
      }
  
      // Attach event listener for resize events
      window.addEventListener('resize', handleResize);
  
      // Initial update on mount
      updateZoomLevel();
  
      // Cleanup function to remove the event listener
      return () => {
        window.removeEventListener('resize', handleResize);
      };
    });
  
    // Reactivity for visibility based on index
    $: isVisible = index > 0;
    $: LogoisVisible = index == 0;
  </script>
  
  <style>
    .center {
      display: block;
      margin-left: auto;
      margin-right: auto;
      width: 50%; /* Adjust as per your requirement */
      height: auto; /* Maintains aspect ratio */
      transition: opacity 2s;
    }
  
    .absolute-center {
      position: absolute;
      left: 50%;
      top: 50%;
      transform: translate(-50%, -50%);
    }
  
    .fade {
      opacity: 0;
      transition: opacity 2s ease-in-out;
    }
  
    .fade-in {
      opacity: 1;
    }
  </style>
{#if LogoisVisible}
    <img src={`${base}/F1.svg.png`} alt="F1 Logo" class="center absolute-center fade-in" in:fade={{ duration: 1000 }}/>
{/if}
