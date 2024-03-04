<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    import { fade } from 'svelte/transition';
    export let index;
    let isVisible = false;
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
    // !! CHANGE WHEN NEED CIRCUIT MAP!!
    $: if (index == 15) {
        isVisible = true;
    } else if (index > 17 && index < 23) {
        isVisible = true;
    } else {
        isVisible = false;
    }
  </script>
  
  <style>
    .center {
        display: block;
        position: absolute;
        margin-top: 12.5%;
        margin-left: 25%;
        margin-right: auto;
        width: 50%; /* Adjust as per your requirement */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
    }
  
    .fade-in {
      opacity: 1;
    }
  </style>

{#if isVisible}
    <img src="abu-dhabi.png" alt="Yas Marina Circuit" class="center fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}