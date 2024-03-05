<script>
    import { onMount } from 'svelte';
    import { base } from '$app/paths';
    export let index;
  
    let carPosition = { x: 0, y: 0 }; // Initial car position
    let telemetryData = []; // This will hold the fetched telemetry data
  
    // Function to fetch telemetry data
    async function fetchTelemetryData() {
      const response = await fetch(`${base}/ver_tele.json`);
      telemetryData = await response.json();
      // Assuming the JSON structure is an array of data points
      carPosition = calculateCarPosition(index); // Initialize the car position
    }
  
    // A function that calculates the car's position based on the index
    function calculateCarPosition(index) {
      // Ensure that the index is within the bounds of the telemetry data array
      if (index < telemetryData.length) {
        const dataPoint = telemetryData[index];
        return {
          x: dataPoint.X,
          y: dataPoint.Y
        };
      }
      return carPosition; // Return current position if index is out of bounds
    }
  
    onMount(() => {
      fetchTelemetryData(); // Fetch telemetry data when the component is mounted
    });
  
    $: if (telemetryData.length > 0) {
      carPosition = calculateCarPosition(index);
    }
</script>

<style>
    .svg-container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    }
</style>
  
<div class="svg-container">
    <svg width="500" height="500" xmlns="http://www.w3.org/2000/svg">
        <circle cx={carPosition.x} cy={carPosition.y} r="10" fill="red" />
    </svg>
</div>