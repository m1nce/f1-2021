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
    $: h2 = index > 23 && index < 27;
    $: Yup = index == 27;
    $: Future = index >=28 && index <29;
    $: s1 = index == 25;
    $: s2 = index == 26;
    $: s3 = index == 27;
    $: s4 = index == 28;
    $: s5 = index == 29;
    $: hamilton = index == 29;
    $: controversy = index == 30;
    $: lastlap = index == 31;
    $: reallast = index == 32;
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
    .belowleft-img {
        position: absolute; 
        top: 55%; 
        left: 5%; 
        width: 35%
    }
    .belowright-img {
        position: absolute; 
        top: 55%; 
        left: 56.5%; 
        width: 35%
        
    }
</style>

{#if h2}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        What is a safety car?
    </h>
{/if}
{#if Future}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Back to the Race
    </h>
{/if}
{#if Yup}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        What happens during this period?
    </h>
{/if}

{#if s1}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        In Formula 1, there are two different types of safety cars:<br>
    </p>
    <p class='description' style='top: 45%; left: 22%'in:fade={{ duration: 200, delay: 200}} out:fade={{ duration: 100 }}>
        A physical car on the track <br>
    </p>
    <p class='description' style='top: 45%; left: 73%'in:fade={{ duration: 200, delay: 200}} out:fade={{ duration: 100 }}>
        A virtual safety car <br>
    </p>
    <img src='physicalsafety.png' alt='crash' class='belowleft-img' in:fade={{ duration: 300, delay: 500}} out:fade={{ duration: 100 }}>
    <img src='virtualsafety.png' alt='crash' class='belowright-img' in:fade={{ duration: 300, delay: 500}} out:fade={{ duration: 100 }}>
{/if}

{#if s2}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        In this instance, a safety car was deployed due to an on-track 
        collision from Latifi that obstructed the racing line.
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
        In this particular race, there was uncertainty whether 
        the race would conclude under the safety car, which would freeze 
        the positions and secure Hamilton's victory. In a strategic gamble, 
        Verstappen pitted for fresh, faster tyres, betting on the chance of 
        the safety car being withdrawn for at least one more racing lap.
    </p>
    <img src='pit-stop.jpeg' alt='rb-pit-stop' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}
{#if hamilton}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Hamilton's Dilemma
    </h>
{/if}
{#if s5}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        Since Hamilton was in the lead and the gap to Verstappen 
        was not sufficient enough to pit and rejoin the race as 1<sup>st</sup>, 
        he was forced to stay out on his old tyres, leaving him at a disadvantage.
    </p>
    <img src='mercedescar.avif' alt='mercedes' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}
{#if controversy}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Where the Controversy Lies
    </h>
{/if}
{#if controversy}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        When Verstappen pitted, cars that were a lap behind Hamilton and Verstappen were in-between
        their cars (Lap 56 rather than 57). Under normal procedures, all lapped cars would unlap
        themselves. This procedure would give Hamilton an advantage as he would have a buffer from Verstappen 
        and an easier time mainintaing his lead. But in this race, only the cars between Verstappen and Hamilton were unlapped.
    </p>
{/if}
{#if lastlap}
    <img src="safety-car.png" alt="safety car" class="safety-car" in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
    <h class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
        Where the Controversy Lies
    </h>
{/if}
{#if lastlap}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        Thus, the race began with Hamilton on old tyres with Verstappen breathing down his neck
        with new and fast tyres.
    </p>
{/if}
{#if reallast}
    <div>
    <h2 class='h2'>
            And the rest... Is History
        </h2>
    </div>
{/if}

