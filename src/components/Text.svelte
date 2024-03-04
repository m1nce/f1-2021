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

    onMount(() => {

  });
  
    // Reactivity for visibility based on index
    $: h1 = index > 0 && index < 9;
    $: s1 = index > 1 && index < 5;
    $: p1 = index > 2 && index < 5;
    $: img1 = index == 3 || index == 4;
    $: p2 = index > 3 && index < 5;
    $: s2 = index == 5;
    $: s3 = index == 6 || index == 7;
    $: s4 = index == 7;
    $: s5 = index == 8;
    $: s6 = index > 10 && index < 15;
    $: p3 = index > 11 && index < 15;
    $: p4 = index > 12 && index < 15;
    $: s7 = index == 14;
    $: s8 = index == 15;
    $: s9 = index == 16;
    $: s10 = index == 17;
    $: s11 = index == 18;
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

    .paragraph1 {
        display: block;
        position: absolute;
        top: 32.5%; /* Center vertically */
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
        top: 40%; /* Center vertically */
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
        top: 40%;
        left: 80%;
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 30%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
    }

    .subtitle2 {
        display: block;
        position: absolute;
        top: 30%; /* Center vertically */
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
        top: 50%; /* Center vertically */
        left: 30%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 40%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .yasmarina {
        display: block;
        position: absolute;
        top: 45%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 70%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 100px;
        font-family: 'Formula1-Bold';
        color: red;
    }

    .description {
        display: block;
        position: absolute;
        top: 15%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 70%; /* Adjust width as needed */
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
    <p class='subtitle1' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Formula 1 is the highest class of international racing: 
    </p>
{/if}

{#if p1}
    <p class='paragraph1' in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
        &#x2022; Open Wheel
    </p>
{/if}

{#if img1}
    <img src="openwheel.jpg" alt="open wheel car" class="right-img" in:fade={{ duration: 600 }} out:fade={{ duration: 100 }}>
{/if}

{#if p2}
    <p class='paragraph2' in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
        &#x2022; Single Seater
    </p>
{/if}

{#if s2}
    <p class='subtitle2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        It consists of a season, which is a series of races, also known as Grand Prix. 
    </p>
    <img src="2021calendar.jpeg" alt="calendar" class="right-img" style="width: 25%;" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s3}
    <p class='subtitle2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        In a season, a number of teams and drivers compete, 
        with each team typically having two drivers race for them.
    </p>
    <img src="drivers.jpeg" alt="drivers" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 1 }}>
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

{#if s6}
    <p class='subtitle1' style='left: 30%; width: 45%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        In the last race of the 2021 Formula 1 season, there were two storylines:
    </p>
{/if}

{#if p3}
    <p class='paragraph1' style='left:30%' in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
        &#x2022; Max Verstappen's 1<sup>st</sup> championship
    </p>
    <img src="mv33.webp" alt="max verstappen" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 1 }}>
{/if}

{#if p4}
    <p class='paragraph2' style='left:30%' in:fade={{ duration: 200 }} out:fade={{ duration: 100 }}>
        &#x2022; Lewis Hamilton's 8<sup>th</sup> championship
    </p>
    <img src="lh44.jpeg" alt="lewis hamilton" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 1 }}>
{/if}

{#if s7}
    <p class='subtitle3' style='top: 55%; width: 45%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        And almost by fate itself, the two drivers had the same number of 
        points entering the last race of the season at Abu Dhabi's...
    </p>
    <img src="2021points.png" alt="points after saudi gp" class="right-img" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s8}
    <p class='yasmarina' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        YAS MARINA CIRCUIT
    </p>
{/if}

{#if s9}
    <p class='subtitle1' style='top: 40%; left: 30%; width: 45%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Before every race, there is always a qualifying session, in which drivers 
        must achieve the fastest lap time to determine their starting position 
        on the "grid."
    </p>
    <img src="grid.jpeg" alt="empty grid" class="right-img" style='top: 45%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s10}
    <p class='subtitle1' style='top: 40%; left: 30%; width: 45%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        In this session, Max Verstappen gets the first position, with 
        Lewis Hamilton right behind him at second.
    </p>
    <img src="abudhabi-qualifying.png" alt="abu dhabi qualifying" class="right-img" style='left: 75%; top: 45%; width: 40%' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
{/if}

{#if s11}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        However, at the start of the race, Hamilton got a better start than Verstappen, 
        leading to Hamilton taking the lead instead of Verstappen.
    </p>
{/if}