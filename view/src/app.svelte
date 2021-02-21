<script>
  import {
    ComposedModal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Checkbox,
    NumberInput,
    Button
  } from 'carbon-components-svelte';
  // import { Game } from './game.svelte';


  let initialised = false;
  let checked = false;
  let gridSize = 5;
  let numTurtles = 1;
  let initSugars = 10;

  // function getRand() {
  //   fetch("./rand")
  //     .then(d => d.text())
  //     .then(d => (rand = d));
  // }

  function configureDetails() {
    initialised = true;
    console.log({ checked, initialised, gridSize });
    fetch('./model', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ gridSize, numTurtles, initSugars })
    });
  }

  function nextTick() {
    fetch('./model')
      .then(res => res.text())
      .then(d => console.log(d));
  }

</script>

<main>
  <h1>SugarScape</h1>
  
  <ComposedModal open={!initialised} on:submit={configureDetails} preventCloseOnClickOutside>
    <ModalHeader title="Configure Sugar Scape Model" />
    <ModalBody hasForm>
      <NumberInput
        min={5}
        max={50}
        bind:value={gridSize}
        invalidText="Number must be between 5 and 50."
        helperText="Size of the grid holding the SugarScape universe."
        label="SugarScape grid size (5 min, 50 max)"
      />

      <NumberInput
        min={1}
        max={10}
        bind:value={numTurtles}
        invalidText="Number must be between 1 and 10."
        helperText="Number of initial turtles"
        label="Number of turtles (1 min, 10 max)"
      />

      <NumberInput
        min={10}
        max={25}
        bind:value={initSugars}
        invalidText="Number must be between 1 and 25."
        helperText="Number of initial sugar"
        label="Number of sugars (10 min, 25 max)"
      />
      <Checkbox labelText="I have reviewed the changes" bind:checked />
    </ModalBody>
    <ModalFooter primaryButtonText="Confirm changes" primaryButtonDisabled={!checked} />
  </ComposedModal>


  <Button on:click={nextTick}>Tick!</Button>

</main>



<style>
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