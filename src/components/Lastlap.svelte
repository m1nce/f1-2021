<script>
  import { onMount } from 'svelte';
  export let index;
  import { fade } from 'svelte/transition';
  let animator = false;
  let verlapData = [], hamlapData = [];
  let animatedVerPoints = [], animatedHamPoints = [];
  let idealmap = [];
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
  const ver_response = await fetch('ver_lap_58.json');
  const ver_data = await ver_response.json(); // This should be an array
  const ham_response = await fetch('ham_lap_58.json');
  const ham_data = await ham_response.json(); // This should be an array
  const ideal_response = await fetch('ver_lap_21.json');
  const ideal_data = await ideal_response.json();
  idealmap = ideal_data.map(transformPoint);
  verlapData = ver_data.map(transformPoint);
  hamlapData = ham_data.map(transformPoint);
  
  });
  function animateLaps() {
  let totalDelayVer = 22000, totalDelayHam = 22000;

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
  $: if (index == 32) {
      animator = true;
      animateLaps();
  } else {
      animator = false;
  }
</script>
<style>
  .track-container {
  position: absolute;
  top: 15%;
  margin-left: -5%;
  left: 30%;
  width: 80%;
  height: 80%;
  z-index: 1; /* Lower z-index than the video */
}

.video-container {
  top: 30%;
  width: 50%;
  height: 50%;
  left: 4%;
  position: absolute; /* This ensures z-index is applied */
  z-index: 99999; /* Higher z-index to ensure it's on top */
  /* Other styling here */
}
</style>

{#if animator}
<div class="track-container">
  <svg class="track-container" viewBox="0 0 100 100">
      <path d={generatePathD(verlapData)} fill="none" stroke="grey" stroke-width="3" />
      <path d={generatePathD(hamlapData)} fill="none" stroke="grey" stroke-width="3"/>
      {#each animatedVerPoints as point}
      <circle cx={(point.Y)} cy={(point.X)} r="1" fill="red" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
      {/each}
      {#each animatedHamPoints as point}
          <circle cx={(point.Y)} cy={(point.X)} r="1" fill="blue" in:fade={{ duration: 1000 }} out:fade={{ duration: 100 }}/>
      {/each}
    </svg>
</div>
<div class="video-container">
  <!-- svelte-ignore a11y-media-has-caption -->
  <video src="winner.mp4" controls width="100%" height="100%" autoplay muted></video>
</div>
{/if}