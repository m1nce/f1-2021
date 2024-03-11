<script>
    import { onMount } from 'svelte';
    import { fade } from 'svelte/transition';
    export let index;
    let isVisible = false;
    let animator = false;
    let topdown = false;
    let verlapData = [], hamlapData = [];
    let idealmap = [];
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
    const ideal_response = await fetch('ver_lap_21.json');
    const ideal_data = await ideal_response.json();
    idealmap = ideal_data.map(transformPoint);
    verlapData = ver_data.map(transformPoint);
    hamlapData = ham_data.map(transformPoint);
    console.log(hamlapData);
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
    $: if (index == 18) {
        animator = true;
        animateLaps();
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
    .big {
        display: block;
        position: absolute;
        width: 100%; /* Adjust as per your requirement */
        height: 100%; /* Maintains aspect ratio */
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
  </style>

{#if animator}
    <div class="track-container">
        <svg class="track-container" viewBox="0 0 100 100">
            <path d={generatePathD(idealmap)} fill="none" stroke="grey" stroke-width="3.5" />
            {#each animatedVerPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r="1" fill="red" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
            {/each}
            {#each animatedHamPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r="1" fill="blue" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
            {/each}
          </svg>
      </div>
{/if}
{#if topdown}
    <img src="yasmarina_irl.jpg" alt="Yas Marina Circuit" class="big fade-in" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
{/if}