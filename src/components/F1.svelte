<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    import { fade } from 'svelte/transition';
    export let index;
    let zoomLevel;
  
    onMount(() => {
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
  
    // Reactivity for visibility based on index
    $: logo = index == 0 || index == 7 || index == 8;
    $: yearAnimation = index == 8;
  </script>
  
  <style>
    .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%; /* Adjust as per your requirement */
        height: auto; /* Maintains aspect ratio */
        transition: all 0.5s ease; /* Smooth transition for all properties */
        background-color: transparent;
        z-index:-10;
    }
  
    .absolute-center {
        position: absolute;
        left: 50%;
        top: 45%;
        transform: translate(-50%, -50%);
        background-color: transparent;
    }
  
    .fade-in {
        opacity: 1;
    }

    .smaller {
        position: absolute; /* Position absolutely within a relative container */
        left: 12.5%; /* Align to the left */
        top: 7.5%; /* Align to the top */
        width: 20%; /* Adjust as per your requirement */
        height: auto; /* Maintains aspect ratio */
        transition: all 0.5s ease; /* Smooth transition for all properties */
        background-color: transparent;
        z-index:-10;
    }

    .year {
        position: absolute;
        font-family: 'Formula1-Bold';
        font-size: 80px;
        color: red;
        top: 55%;
        left: 70%;
        transition: transform 0.5s ease, font-size 0.5s ease, top 0.5s ease, left 0.5s ease; /* Adjust transition properties as needed */
        z-index:-10;
    }

    .yearsmaller {
        position: absolute; /* Position absolutely within a relative container */
        left: 20.5%; /* Align to the left */
        top: 11.5%; /* Align to the top */
        transition: all 0.5s ease; /* Smooth transition for all properties */
        color: red;
        font-family: 'Formula1-Bold';
        font-size: 16px;
        z-index:-10;
    }
  </style>

<img src={`${base}/F1.svg.png`} alt="F1 Logo" class="{logo ? 'center' : 'smaller'} absolute-center fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 1000 }}/>
{#if index >= 8}
    <h class='{yearAnimation ? 'year' : 'yearsmaller'}' in:fade={{ duration: 800 }} out:fade={{ duration: 100 }}>
            2021
    </h>
{/if}