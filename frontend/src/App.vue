<script setup>
import axios from "axios";

async function testBackend() {
  try {
    const response = await axios.get(
      "http://127.0.0.1:8000/test"
    );

    alert(
      JSON.stringify(response.data)
    );

  } catch (error) {

    console.error(error);

    alert("Backend connection failed");
  }
}
</script>

<template>

  <h1>DeepBlocks</h1>

  <button @click="testBackend">
    Test Backend
  </button>

</template>