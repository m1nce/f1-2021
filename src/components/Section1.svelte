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
            font-family: 'Formula1-Regular';
            src: url('${base}/Formula1-Regular.otf') format('opentype');
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
    $: h1 = index > 0 && index < 7;
    $: s1 = index == 2;
    $: s2 = index == 3;
    $: s3 = index == 4 || index == 5;
    $: s4 = index == 5;
    $: s5 = index == 6;
</script>

<style>
    @font-face {
        font-family: 'Formula1-Regular';
        src: url('Formula1-Regular.otf') format('opentype');
    }

    @font-face {
        font-family: 'Formula1-Wide';
        src: url('Formula1-Wide.otf') format('opentype');
    }

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
        top: 40%; /* Center vertically */
        left: 35%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .paragraph1 {
        display: block;
        position: absolute;
        top: 47.5%; /* Center vertically */
        left: 20%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .paragraph2 {
        display: block;
        position: absolute;
        top: 55%; /* Center vertically */
        left: 20%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .right-img {
        display: block;
        position: absolute;
        top: 50%;
        left: 80%;
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 30%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
    }

    .subtitle2 {
        display: block;
        position: absolute;
        top: 45%; /* Center vertically */
        left: 30%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 40%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .subtitle3 {
        display: block;
        position: absolute;
        top: 60%; /* Center vertically */
        left: 30%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 40%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }
</style>

{#if h1}
    <h in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        What is Formula 1?
    </h>
{/if}

{#if s1}
    <p class='subtitle1' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Formula 1 is the highest class of international racing:
    </p>
    <p class='paragraph1' in:fade={{ duration: 200, delay: 600}} out:fade={{ duration: 100 }}>
        &#x2022; Open Wheel
    </p>
    <p class='paragraph2' in:fade={{ duration: 200, delay: 800 }} out:fade={{ duration: 100 }}>
        &#x2022; Single Seater
    </p>
    <img src="openwheel.jpg" alt="open wheel car" class="right-img" in:fade={{ duration: 600, delay: 200 }} out:fade={{ duration: 100 }}>
{/if}

{#if s2}
    <p class='subtitle2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        It consists of a season, which is a series of races, each known as a Grand Prix.
    </p>
    <img src="2021calendar.jpeg" alt="calendar" class="right-img" style="width: 25%;" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s3}
    <p class='subtitle2' style="top:40%" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        In a season, a number of teams compete,
        with each team typically having two drivers race for them.
    </p>
    <img src="f1team.jpeg" alt="drivers" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 1 }}>
{/if}

{#if s4}
    <p class='subtitle3' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        At the end of a season, there are two winners - a driver and a team - dependent on a points system.
    </p>
    <img src="podium.avif" alt="podium" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s5}
    <p class='subtitle2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Each Grand Prix gives a certain number of points to drivers and their team, 
        depending on where they finished from positions 1-10.
    </p>
    <img src="championship_points.jpg" alt="championship pts" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}