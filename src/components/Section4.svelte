<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    import { fade } from 'svelte/transition';
    import confetti from 'canvas-confetti';
    export let index;
    let zoomLevel;
    let legends = [
        { id: 'hamilton', color: 'blue', text: 'Hamilton'},
        { id: 'verstappen', color: 'red', text: 'Verstappen'},
        { id: 'perez', color: 'green', text: 'Perez'},
        { id: 'latifi', color: 'silver', text: 'Latifi'},
        { id: 'schumacher', color: 'black', text: 'Schumacher'},
    ];
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

    function launchConfetti() {
        confetti({
            particleCount: 1000,
            angle: 90,
            spread: 200,
        });
    }

    let final = false;
    // Reactivity for visibility based on index
    $: h2 = index > 21 && index < 25;
    $: Yup = index == 25;
    $: Future = index >= 26 && index < 27;
    $: s1 = index == 23;
    $: s2 = index == 24;
    $: s3 = index == 25;
    $: s4 = index == 26;
    $: s5 = index == 27;
    $: hamilton = index == 27;
    $: controversy = index == 28;
    $: lastlap = index == 29;
    $: reallast = index == 30;
    $: if (index === 31) {
        final = true;
    } else {
        final = false;
    }

    // React to changes in the 'final' variable
    $: if (final) {
        setTimeout(launchConfetti, 3000); // Delay of 1400ms before launching confetti
        setTimeout(launchConfetti, 3300);
        setTimeout(launchConfetti, 3600);
    }
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
        font-family: 'Formula1-Bold';
        z-index: -10;
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
    .top-img {
        position: absolute; 
        top: 6%;
        width: 30%;
    }
    .legend {
        position: absolute;
        right: 10px; /* Position to the right */
        top: 40%; /* Position from the top */
        padding: 10px;
        background-color: transparent; /* Background of the legend */
        border-radius: 5px;
        font-family: 'Formula1-Regular';
        z-index:-10;
    }

    .legend-entry {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
        z-index:-10;
    }

    .legend-color {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 10px;
        z-index:-10;
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
        During a safety car period, all cars are required to reduce speed and forbidden 
        from overtaking each other on the track, ensuring safety. <br><br>This 
        slowdown often presents a strategic opportunity for teams to pit 
        and change tyres.
    </p>
    <img src='safety-car-rules.webp' alt='safety-car' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}

{#if s4}
    <p class='description' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        In this race, there was a chance it might end under the safety car, 
        locking the positions and ensuring Hamilton's win.
        <br><br>
        Verstappen took a risk by switching to new, quicker tyres, hoping for at 
        least one more lap of active racing after the safety car leaves.
    </p>
    <img src='pit-stop.jpeg' alt='rb-pit-stop' class='below-img' style='top:50%' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
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
    <p class='description' style='top: 37.5%' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
        During Verstappen's pit stop, there were cars one lap behind him and Hamilton, 
        sandwiched between them. 
        <br><br>
        Normally, all lapped cars would move ahead to rejoin the race pace, 
        which could have ended the race under the safety car since the procedure 
        would've taken too long, favoring Hamilton. 
        <br><br>
        However, in this case, only those lapped cars directly between Verstappen 
        and Hamilton were allowed to unlap, altering the expected advantage for Hamilton.
    </p>
    <img src='safety.jpg' alt='maxbreathe' class='below-img' style='top: 57%' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
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
    <img src='breathing.png' alt='maxbreathe' class='below-img' in:fade={{ duration: 300 }} out:fade={{ duration: 100 }}>
{/if}

{#if reallast}
    <div>
        <h2 class='h2' in:fade={{ duration: 400 }} out:fade={{ duration: 100 }}>
                And the rest... is history
        </h2>
        <div class="legend">
            {#each legends.slice(0,2) as legend}
                <div class="legend-entry">
                <div class="legend-color" style="background-color: {legend.color};"></div>
                <div>{legend.text}</div>
                </div>
            {/each}
        </div>
    </div>
{/if}

{#if final}
<img src='newspaper.png' alt='headline' class='top-img' style='left:35%' in:fade={{ duration: 400, delay: 200}} out:fade={{ duration: 100 }}>
    <img src='crying-tyre.jpeg' alt='crying tyre' class='below-img' style='left:5%' in:fade={{ duration: 600, delay: 1500}} out:fade={{ duration: 100 }}>
    <img src='2021podium.jpeg' alt='abu dhabi podium' class='below-img' style='left:50%; width:37.5%' in:fade={{ duration: 600, delay: 3000}} out:fade={{ duration: 100 }}>
{/if}