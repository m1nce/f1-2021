<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    import { fade } from 'svelte/transition';
    export let index;
    let zoomLevel;
  
    onMount(() => {
        // Add text font
        const style = document.createElement('style');
        style.textContent = `
        @font-face {
            font-family: 'Formula1-Bold';
            src: url('${base}/Formula1-Bold.otf') format('opentype');
        }
        `;
        document.head.appendChild(style);

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

    onMount(() => {

  });
  
    // Reactivity for visibility based on index
    let h1 = false;
    let s1 = false;
    $: if (index > 0) {
        h1 = true;
    } else {
        h1 = false;
    }

    $: if (index > 1) {
        s1 = true;
    } else {
        s1 = false;
    }
  </script>
  
  <style>
    h {
        display: block;
        position: absolute;
        top: 12.5%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 36px;
        font-family: 'Formula1-Bold'
    }

    .subtitle1 {
        display: block;
        position: absolute;
        top: 25%; /* Center vertically */
        left: 35%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }
  </style>
  
{#if h1}
    <h in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        So what is Formula 1?
    </h>
{/if}

{#if s1}
    <p class='subtitle1' in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
        Formula 1 is the highest class of international racing:
    </p>
{/if}