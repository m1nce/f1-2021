<script>
    import { onMount } from 'svelte';
  
    export let index;
    let isVisible = false;
    let zoomLevel;
  
    // This will run only on the client side
    onMount(() => {
      function updateZoomLevel() {
        const screenWidth = window.innerWidth;
        zoomLevel = screenWidth <= 600 ? 4 : 5.85; // adjust values as needed
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
  
    // Reactivity statement to update visibility based on index
    $: isVisible = true;
  </script>
  
  <!-- Conditional rendering for the image based on isVisible -->
  {#if isVisible}
    <img src="abu-dhabi.avif" alt="Yas Marina Circuit" />
  {/if}
  
  <!-- Placeholder for your d3 container, visible regardless of index -->
  <svg id='d3-container'></svg>
  
<!-- Conditional rendering for the image based on isVisible -->
<img src="abu-dhabi.avif" alt="Yas Marina Circuit" class:visible={isVisible}/>

<!-- Placeholder for your d3 container, visible regardless of index -->
<svg id='d3-container'></svg>

<style>
    /* Example CSS, adjust as needed */
    #d3-container {
        width: 100%;
        height: 100%; /* Adjust based on your needs */
    }

    img {
        width: 75%; /* Ensure the image is responsive */
        display: block; /* Adjust as needed */
        position: absolute;
        align-items: center;
        left: 12.5%;
        top: 12.5%;
        transition: opacity 2s, visibility 2s;
    }

    .visible {
        display: block;
    }

    img:not(.visible) {
        display: none;
    }
</style>