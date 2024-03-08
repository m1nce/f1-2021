<script>
    import { onMount } from 'svelte';
    export let index;
    import { fade } from 'svelte/transition';
    let animator = false;
    let msclapData = [], hamlapData = [], latlapData = [];
    let animatedmscPoints = [], animatedHamPoints = [], animatedlatPoints = [];
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
    const msc_response = await fetch('MSC_lap_53.json');
    const msc_data = await msc_response.json(); // This should be an array
    const ham_response = await fetch('ham_lap_21.json');
    const ham_data = await ham_response.json(); // This should be an array
    const lat_response = await fetch('lat_lap_53.json');
    const lat_data = await lat_response.json();
    msclapData = msc_data.map(transformPoint);
    hamlapData = ham_data.map(transformPoint);
    latlapData = lat_data.map(transformPoint);
    animateLaps();
    });
    function animateLaps() {
    let totalDelaymsc = 0, totalDelayHam = 0, totalDelaylat = 0;

    msclapData.forEach((point, index) => {
        const delaymsc = index === 0 ? 0 : point.Time - msclapData[index - 1].Time;
        totalDelaymsc += delaymsc;
        setTimeout(() => {
            animatedmscPoints = [point]; // Set the array to only contain the current point
            // Trigger Svelte to re-render by assigning a new array object
            animatedmscPoints = animatedmscPoints.slice();
        }, totalDelaymsc);
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
    latlapData.forEach((point, index) => {
        const delaylat = index === 0 ? 0 : point.Time - latlapData[index - 1].Time;
        totalDelaylat += delaylat;
        setTimeout(() => {
            animatedlatPoints = [point]; // Set the array to only contain the current point
            // Trigger Svelte to re-render by assigning a new array object
            animatedlatPoints = animatedlatPoints.slice();
        }, totalDelaylat);
    });
}
$: if (index === 22 || index === 23) {
    animator = true;
} else {
    animator = false;
}
</script>
  
  <style>
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
            <path d={generatePathD(msclapData)} fill="none" stroke="grey" stroke-width="3" />
            {#each animatedmscPoints as point}
            <circle cx={(point.Y)} cy={(point.X)} r="1" fill="purple" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
            {/each}
            {#each animatedlatPoints as point}
                <circle cx={(point.Y)} cy={(point.X)} r="1" fill="green" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
            {/each}
          </svg>
      </div>
{/if}