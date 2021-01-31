<script>
  /** Gray 10 theme **/
  import { Button } from "carbon-components-svelte";
  import { Toggle } from "carbon-components-svelte";

  let rand = -1;
  function getRand() {
    fetch("./rand")
      .then(d => d.text())
      .then(d => (rand = d));
  }
  getRand();
</script>

<main>
  <h1>Satya your number is {rand}!!!!!!</h1>
  <Button on:click={getRand} kind="secondary">Random number</Button>
  <Toggle labelText="Push notifications" />
</main>


<style>
  /** Carbon Gray 10 theme **/
  @import "carbon-components-svelte/css/g10";
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>