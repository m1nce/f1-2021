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
    
    let legends = [
        { id: 'hamilton', color: 'blue', text: 'Hamilton'},
        { id: 'verstappen', color: 'red', text: 'Verstappen'},
        { id: 'perez', color: 'green', text: 'Perez'},
        { id: 'latifi', color: 'silver', text: 'Latifi'},
        { id: 'schumacher', color: 'black', text: 'Schumacher'},
    ];
  
    // Reactivity for visibility based on index
    $: s11 = index == 16;
    $: s12 = index == 17;
    $: s13 = index == 18;
    $: s14 = index == 19;
    $: s15 = index == 20 || index == 21;
    $: s16 = index == 21;
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

    .description {
        display: block;
        position: absolute;
        top: 17.5%; /* Center vertically */
        left: 50%; /* Center horizontally */
        transform: translate(-50%, -50%); /* Offset by half of the width and height */
        width: 70%; /* Adjust width as needed */
        height: auto; /* Maintains aspect ratio */
        transition: opacity 2s;
        text-align: center; /* Center text horizontally within the element */
        font-size: 2.5vh;
        font-family: 'Formula1-Regular'
    }

    .legend {
        position: absolute;
        right: 10px; /* Position to the right */
        top: 40%; /* Position from the top */
        padding: 10px;
        background-color: transparent; /* Background of the legend */
        border-radius: 5px;
        font-family: 'Formula1-Regular';
    }

    .legend-entry {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }

    .legend-color {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        margin-right: 10px;
    }

</style>

{#if s11}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        However, at the start of the race, Hamilton got a better start than Verstappen, 
        leading to Hamilton taking the lead instead of Verstappen.
    </p>
    <div class="legend">
        {#each legends.slice(0, 2) as legend}
            <div class="legend-entry">
            <div class="legend-color" style="background-color: {legend.color};"></div>
            <div>{legend.text}</div>
            </div>
        {/each}
    </div>
{/if}

{#if s12}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        Max Verstappen pits for newer tyres, as each driver is mandated to have 
        at least one pit stop in a race.
    </p>
    <div class="legend">
        {#each legends.slice(0, 2) as legend}
            <div class="legend-entry">
            <div class="legend-color" style="background-color: {legend.color};"></div>
            <div>{legend.text}</div>
            </div>
        {/each}
    </div>
{/if}

{#if s13}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        Hamilton pits to ensure he doesn't lose lap time
        by staying on old tyres that are losing grip. Verstappen's teammate, 
        Sergio Perez, takes 1<sup>st</sup> place.
    </p>
    <div class="legend">
        {#each legends.slice(0, 3) as legend}
            <div class="legend-entry">
            <div class="legend-color" style="background-color: {legend.color};"></div>
            <div>{legend.text}</div>
            </div>
        {/each}
    </div>
{/if}

{#if s14}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        Hamilton finally passes Perez after a lengthy one-and-a-half lap tussle. 
        However, Perez played the ultimate team game: defending long enough to bring 
        Verstappen back into the race.
    </p>
    <div class="legend">
        {#each legends.slice(0, 3) as legend}
            <div class="legend-entry">
            <div class="legend-color" style="background-color: {legend.color};"></div>
            <div>{legend.text}</div>
            </div>
        {/each}
    </div>
{/if}

{#if s15}
    <p class='description' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        Nicholas Latifi (dubbed Crashtifi by F1 fans) crashes into the barriers while racing 
        Mick Schumacher and prompts a safety car.
    </p>
    <div class="legend">
        {#each legends.slice(3,) as legend}
            <div class="legend-entry">
            <div class="legend-color" style="background-color: {legend.color};"></div>
            <div>{legend.text}</div>
            </div>
        {/each}
    </div>
{/if}

{#if s16}
    <p class='description' style='top: 90%' in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}>
        But what is a safety car?
    </p>
{/if}

