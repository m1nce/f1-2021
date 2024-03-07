<script>
        import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    export let index;
    let isVisible = false;
    let animator = false;
    let topdown = false;
    let lapData = {
        ver: [],
        ham: []
    };
    let animatedPoints = {
        ver: [],
        ham: []
    };
    let currentLap = 'initial'; // To keep track of which lap data to display

    const min_x = -2180, min_y = -5351;
    const scale_factor = 0.005839075090505664;
    const offset_x = 26.68749270115614, offset_y = 0;

    function transformPoint(point) {
        return {
            X: (point.X - min_x) * scale_factor + offset_x,
            Y: (point.Y - min_y) * scale_factor + offset_y,
            Time: point.Time // Include Time in transformed data
        };
    }

    const generatePathD = (data) => {
        return data.map((point, index) => {
            const command = index === 0 ? 'M' : 'L';
            return `${command}${point.Y},${point.X}`; // Adjusting coordinates
        }).join(' ');
    };

    async function fetchLapData(fileName) {
        const response = await fetch(fileName);
        return response.json(); // Assuming the fetched data is an array
    }

    onMount(async () => {
        const laps = ['ver_first_lap.json', 'ver_pitstop_lap.json', 'ham_first_lap.json', 'ham_regular_lap.json'];
        const [verFirstLap, verPitstopLap, hamFirstLap, hamRegularLap] = await Promise.all(laps.map(lap => fetchLapData(lap)));
        
        lapData.ver = [verFirstLap.map(transformPoint), verPitstopLap.map(transformPoint)];
        lapData.ham = [hamFirstLap.map(transformPoint), hamRegularLap.map(transformPoint)];
        
        // Optionally, start animation or display initial lap here
    });

    // Example function to change the displayed lap based on index or other conditions
    function updateLapDisplay() {
        if (index == 19) {
            currentLap = 'verPitstop'; // Adjust based on your conditions
        } else {
            currentLap = 'initial'; // Reset to initial condition
        }
        // Reset animation or update lap display logic here
    }

    // Call this function when you need to update the lap display
    $: updateLapDisplay();

    // Reactivity for visibility based on index
    // !! CHANGE WHEN NEED CIRCUIT MAP!!
    $: if (index == 15) {
        isVisible = false;
    } else if (index > 19 && index < 24) {
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
    $: if (index == 19) {
        ver_pitstop = true;
    } else {
        ver_pitstop = false;
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
        top: 24%;
        width: 72%; /* Adjust as per your requirement */
        height: 71.5%; /* Maintains aspect ratio */
        margin-left: 13.3%;
        margin-right: auto;
        transition: opacity 2s;
    }
    .fade-in {
      opacity: 1;
    }
    .track-container {
        position: absolute; /* The parent container is set to position: relative */
        top:5%;
        margin-left:0%;
        width:  100%/* width of your track image */;
        height: 100%/* height of your track image */;
        }
    polyline {
        fill: grey;
        stroke-width: 6; /* Adjust as needed */
    }
  </style>

{#if isVisible}
    <img src="abu-dhabi.png" alt="Yas Marina Circuit" class="center fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}
{#if animator}
    <div class="track-container">
        <svg class="track-container" viewBox="0 0 100 100">
            <path d={generatePathD(hamlapData)} fill="none" stroke="grey" stroke-width="3"/>
            {#each animatedVerPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r=".5" fill="red" />
            {/each}
            {#each animatedHamPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r=".5" fill="blue" />
            {/each}
          </svg>
        
      </div>
{/if}
{#if ver_pitstop}
    <div class="track-container">
        <svg class="track-container" viewBox="0 0 100 100">
            <path d={generatePathD(ham_regular_lap)} fill="none" stroke="grey" stroke-width="3"/>
            {#each animatedVerPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r=".5" fill="red" />
            {/each}
            {#each animatedHamPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r=".5" fill="blue" />
            {/each}
          </svg>
        
      </div>
{/if}
{#if topdown}
    <img src="yasmarina_irl.jpg" alt="Yas Marina Circuit" class="big fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}