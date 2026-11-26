<script setup>

import { ref } from "vue";
import axios from "axios";

const layers = ref([]);
const modelInfo = ref("");
const trainingResults = ref("");

function addConv2D() {
  layers.value.push({
    type: "Conv2D",
    in_channels: 1,
    out_channels: 6,
    kernel_size: 5
  });
}

function addMaxPool() {
  layers.value.push({
    type: "MaxPool2D",
    kernel_size: 2
  });
}

function addFlatten() {
  layers.value.push({
    type: "Flatten"
  });
}

function addLinear() {
  layers.value.push({
    type: "Linear",
    in_features: 576,
    out_features: 10
  });
}

async function sendArchitecture() {

  try {

    const response = await axios.post(
      "http://127.0.0.1:8000/architecture",
      {
        layers: layers.value
      }
    );

    modelInfo.value = response.data.model;

  } catch(error) {

    console.error(error);

    alert("Failed to send architecture");

  }
}

async function trainModel() {

  try {

    trainingResults.value = "Training...";

    const response =
      await axios.post(
        "http://127.0.0.1:8000/train"
      );

    console.log(response.data);

    trainingResults.value =
      JSON.stringify(
        response.data,
        null,
        2
      );

  }
  catch(error){

    console.error(error);

    trainingResults.value =
      "Training failed";

  }
}

</script>

<template>

  <div class="container">

    <div class="left-panel">

      <h2>Blocks</h2>

      <button @click="addConv2D">
        Add Conv2D
      </button>

      <button @click="addMaxPool">
        Add MaxPool
      </button>

      <button @click="addFlatten">
        Add Flatten
      </button>

      <button @click="addLinear">
        Add Linear
      </button>

      <button @click="sendArchitecture">
        Send Architecture
      </button>

      <button @click="trainModel">
        Train Model
      </button>

    </div>

    <div class="workspace">

      <h2>Workspace</h2>

      <div
        v-for="(layer,index) in layers"
        :key="index"
        class="layer-card"
      >

        <h3>
          {{ index + 1 }}.
          {{ layer.type }}
        </h3>

        <div v-if="layer.type === 'Conv2D'">

          In Channels

          <input
            v-model.number="layer.in_channels"
            type="number"
          />

          Out Channels

          <input
            v-model.number="layer.out_channels"
            type="number"
          />

          Kernel Size

          <input
            v-model.number="layer.kernel_size"
            type="number"
          />

        </div>

        <div v-if="layer.type === 'MaxPool2D'">

          Kernel Size

          <input
            v-model.number="layer.kernel_size"
            type="number"
          />

        </div>

        <div v-if="layer.type === 'Linear'">

          In Features

          <input
            v-model.number="layer.in_features"
            type="number"
          />

          Out Features

          <input
            v-model.number="layer.out_features"
            type="number"
          />

        </div>

      </div>

    </div>

    <div class="info-panel">

      <h2>Info</h2>
      <h3>Generated Model</h3>
      <pre>{{ modelInfo }}</pre>
      <h3>
        Training Results
      </h3>

      <pre>
      {{ trainingResults }}
      </pre>
      <p>
        Layer Count:
        {{ layers.length }}
      </p>

    </div>

  </div>

</template>

<style>

.container{
  display:flex;
  height:100vh;
}

.left-panel{
  width:20%;
  border-right:1px solid black;
  padding:20px;
}

.workspace{
  width:55%;
  padding:20px;
}

.info-panel{
  width:25%;
  border-left:1px solid black;
  padding:20px;
}

button{
  display:block;
  margin-bottom:10px;
}

.layer-card{
  border:1px solid gray;
  padding:10px;
  margin-bottom:10px;
}

input{
  display:block;
  margin-bottom:8px;
}

</style>