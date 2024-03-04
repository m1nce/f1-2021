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
    $: h2 = index > 23 && index < 30;
    $: s1 = index == 25;
    $: s2 = index == 26;
    $: s3 = index == 27;
    $: s4 = index == 28;
    $: s5 = index == 29;
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

    .safety-car {
        display: block;
        position: absolute;
        top: 5%;
        left: 50%;
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 70%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        background-color: transparent;
    }

    .h2 {
        display: block;
        position: absolute;
        top: 18%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: auto; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 36px;
        font-family: 'Formula1-Bold'
    }

    .description {
        display: block;
        position: absolute;
        top: 30%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 70%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 20px;
        font-family: 'Formula1-Regular'
    }

    .below-img {
        position: absolute; 
        top: 42.5%; 
        left: 30%; 
        width: 40%
    }
</style>

{#if h2}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        What is a safety car?
    </h>
{/if}

{#if s1}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        In Formula 1, there are two different types of safety cars:<br>
    </p>
    <p class='description' style='top: 37.5%; left: 40%'in:fade={{ duration: 200, delay: 200}} out:fade={{ duration: 100 }}>
        &#x2022; A physical car on track <br>
    </p>
    <p class='description' style='top: 45%; left: 38.5%'in:fade={{ duration: 200, delay: 400}} out:fade={{ duration: 100 }}>
        &#x2022; A virtual safety car <br>
    </p>
{/if}

{#if s2}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        In this instance, a safety car was deployed due to an on-track 
        collision that obstructed the racing line.
    </p>
    <img src='latifi-crash.webp' alt='crash' class='below-img' in:fade={{ duration: 300, delay: 200}} out:fade={{ duration: 100 }}>
{/if}

{#if s3}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        During a safety car period, all cars are required to reduce speed and 
        may not overtake each other on the track, ensuring safety. This 
        slowdown often presents a strategic opportunity for teams to pit 
        and change tyres.
    </p>
    <img src='safety-car-rules.webp' alt='safety-car' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}

{#if s4}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        However, in this particular race, there was uncertainty whether 
        the race would conclude under the safety car, which would freeze 
        the positions and secure Hamilton's victory. In a strategic gamble, 
        Verstappen pitted for fresh, faster tyres, betting on the chance of 
        the safety car being withdrawn for at least one more racing lap.
    </p>
    <img src='pit-stop.jpeg' alt='rb-pit-stop' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}

{#if s5}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        On the other hand, since Hamilton was 1st and the gap to Verstappen 
        was not sufficient enough to pit and rejoin the race as 1st, 
        he was forced to stay out on his old and slower tyres.
    </p>
    <img src='mercedescar.avif' alt='mercedes' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}