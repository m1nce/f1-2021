<script>
    export let index;
    import Section1 from './Section1.svelte';
    import Section2 from './Section2.svelte';
    import Section3 from './Section3.svelte';
    import Section4 from './Section4.svelte';
</script>

<!-- So what is Formula 1? -->
<Section1 {index}/>

<!-- Specifics of 2021 season -->
<Section2 {index}/>

<!-- Race specifics before safety car -->
<Section3 {index}/>

<!-- What is a safety car? -->
<Section4 {index}/>