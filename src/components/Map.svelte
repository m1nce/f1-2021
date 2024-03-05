<script>
    import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    export let index;
    let isVisible = false;
    let animator = false;
    let topdown = false;
    let zoomLevel;
    import { tweened } from 'svelte/motion';
    import { linear, quadIn } from 'svelte/easing';

    // Define the path as an array of [x, y] points
    const lewis_path = [
      { x: 662, y: 360 },   // Start at top-left
      { x: 662, y: 500 },
       // Move to bottom-left
    ];
    const max_path = [
      { x: 685, y: 380 },   // Start at top-left
      { x: 685, y: 450 }, // Move to bottom-left
    ];

    // Create a tweened value for the circle's position
    const lewis_position = tweened(lewis_path[0], { duration: 1000, easing: linear });
    const max_position = tweened(max_path[0], { duration: 2000, easing: linear });

    // Function to animate through the path
    function animateLewis() {
        lewis_path.forEach((pos, i) => {
            setTimeout(() => lewis_position.set(pos), i * 1000);
        });
    }
    function animateMax() {
        max_path.forEach((pos, i) => {
            setTimeout(() => max_position.set(pos), i * 1000);
            });
    }
    $: if (index === 18) {
    animateLewis();
    animateMax();
    }

    onMount(() => {
        animatePath();
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
        isVisible = false;
    } else if (index > 18 && index < 24) {
        isVisible = true;
    } else {
        isVisible = false;
    }
    $: if (index == 18) {
        animator = true;
    } else {
        animator = false;
    }
    $: if (index == 15) {
        topdown = true;
    } else {
        topdown = false;
    }
  </script>
  
  <style>
    .center {
        display: block;
        position: absolute;
        top: 20%;
        margin-left: 25%;
        margin-right: auto;
        width: 50%; /* Adjust as per your requirement */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
    }
    .big {
        display: block;
        position: absolute;
        width: 100%; /* Adjust as per your requirement */
        height: 100%; /* Maintains aspect ratio */
        transition: opacity 2s;
    }
    .yasmarina {
        display: block;
        position: absolute;
        top: 25%;
        width: 70%; /* Adjust as per your requirement */
        height: 70%; /* Maintains aspect ratio */
        margin-left: 15%;
        margin-right: auto;
        transition: opacity 2s;
    }
    .fade-in {
      opacity: 1;
    }
    .lewiscircle {
        position: absolute;
        width: 10px; /* Size of the circle */
        height: 10px; /* Size of the circle */
        background-color: red;
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }
    .maxcircle {
        position: absolute;
        width: 10px; /* Size of the circle */
        height: 10px; /* Size of the circle */
        background-color: blue;
        border-radius: 50%;
        transform: translate(-50%, -50%);
    }
    .track-container {
        position: relative; /* The parent container is set to position: relative */
        width:  100%/* width of your track image */;
        height: 100%/* height of your track image */;
        }

    .track-image {
        position: absolute;
        top: 20%;
        margin-left: 25%;
        margin-right: auto;
        width: 50%;
        height: auto;
        }
  </style>

{#if isVisible}
    <img src="abu-dhabi.png" alt="Yas Marina Circuit" class="center fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}
{#if animator}
    <div class="track-container">
        <img src="abu-dhabi.png" alt="Yas Marina Circuit" class="track-image fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
        <div class="lewiscircle" style="left: {$lewis_position.x}px; top: {$lewis_position.y}px;" />
        <div class="maxcircle" style="left: {$max_position.x}px; top: {$max_position.y}px;" />
      </div>
{/if}
{#if topdown}
    <img src="yasmarina_irl.jpg" alt="Yas Marina Circuit" class="big fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}