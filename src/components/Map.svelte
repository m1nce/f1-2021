<script>
    import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    import { tick } from 'svelte';
    export let index;
    let isVisible = false;
    let animator = false;
    let ver_pitstop = false;
    let topdown = false;
    let verlapData = [], hamlapData = [];
    let animatedVerPoints = [], animatedHamPoints = [];
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
      // Inverting both X and Y values for a 180-degree rotation
      return `${command}${point.Y},${(point.X)}`; // Adjusting Y value to reposition graph if needed
    }).join(' ')};
    onMount(async () => {
    const ver_response = await fetch('ver_first_lap.json');
    const ver_data = await ver_response.json(); // This should be an array
    const ham_response = await fetch('ham_first_lap.json');
    const ham_data = await ham_response.json(); // This should be an array
    verlapData = ver_data.map(transformPoint);
    hamlapData = ham_data.map(transformPoint);


    animateLaps();
    });
    function animateLaps() {
    let totalDelayVer = 0, totalDelayHam = 0;

    verlapData.forEach((point, index) => {
        const delayVer = index === 0 ? 0 : point.Time - verlapData[index - 1].Time;
        totalDelayVer += delayVer;
        setTimeout(() => {
            animatedVerPoints = [point]; // Set the array to only contain the current point
            // Trigger Svelte to re-render by assigning a new array object
            animatedVerPoints = animatedVerPoints.slice();
        }, totalDelayVer);
    });

    hamlapData.forEach((point, index) => {
        const delayHam = index === 0 ? 0 : point.Time - hamlapData[index - 1].Time;
        totalDelayHam += delayHam;
        setTimeout(() => {
            animatedHamPoints = [point]; // Set the array to only contain the current point
            // Trigger Svelte to re-render by assigning a new array object
            animatedHamPoints = animatedHamPoints.slice();
        }, totalDelayHam);
    });
}

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
            <path d={generatePathD(hamlapData)}  fill="none" stroke="grey" stroke-width="3"/>
            {#each animatedVerPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r="1" fill="red" />
            {/each}
            {#each animatedHamPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r="1" fill="blue" />
            {/each}
          </svg>
        
      </div>
{/if}
{#if ver_pitstop}
    <div class="track-container">
        <svg class="track-container" viewBox="0 0 100 100">
            <path d={generatePathD(hamlapData)} fill="none" stroke="grey" stroke-width="3"/>
            {#each animatedVerPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r="1" fill="red" />
            {/each}
            {#each animatedHamPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r="1" fill="blue" />
            {/each}
          </svg>
        
      </div>
{/if}
{#if topdown}
    <img src="yasmarina_irl.jpg" alt="Yas Marina Circuit" class="big fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}