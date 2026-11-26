<script setup>

import { ref } from "vue";
import axios from "axios";

const layers = ref([]);

function addConv2D() {
  layers.value.push({
    type: "Conv2D"
  });
}

function addMaxPool() {
  layers.value.push({
    type: "MaxPool2D"
  });
}

function addFlatten() {
  layers.value.push({
    type: "Flatten"
  });
}

function addLinear() {
  layers.value.push({
    type: "Linear"
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

    alert(
      JSON.stringify(response.data)
    );

  } catch(error) {

    console.error(error);

    alert("Failed to send architecture");

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

    </div>

    <div class="workspace">

      <h2>Workspace</h2>

      <div
        v-for="(layer,index) in layers"
        :key="index"
      >
        {{ index + 1 }}.
        {{ layer.type }}
      </div>

    </div>

    <div class="info-panel">

      <h2>Info</h2>

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

</style>