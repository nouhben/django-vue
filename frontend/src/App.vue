<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="Welcome to Your Vue.js App" />-->
    <!-- {{ msg }} -->

    <div class="container-fluid mb-5">
      <div class="row">
        <div class="col-4 mx-auto">
          <form @submit.prevent="submitForm" class="form-inline">
            <div class="form-group row">
              <input
                type="text"
                class="form-control col-3 my-2"
                placeholder="ID"
                v-model="new_car.car_id"
              />
              <input
                type="text"
                class="form-control col-3 my-2"
                placeholder="Name"
                v-model="new_car.car_name"
              />
              <input
                type="text"
                class="form-control col-3 my-2"
                placeholder="Age"
                v-model="new_car.age"
              />
              <input
                type="text"
                class="form-control col-3 my-2"
                placeholder="Type"
                v-model="new_car.car_type"
              />
              <button class="btn btn-success">submit</button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <table class="table">
      <thead>
        <th>ID</th>
        <th>Name</th>
        <th>Age</th>
        <th>Type</th>
      </thead>
      <tbody>
        <tr v-for="cr in cars" :key="cr.id" @dblclick="$data.new_car = cr">
          <td>{{ cr.car_id }}</td>
          <td>{{ cr.car_name }}</td>
          <td>{{ cr.age }}</td>
          <td>{{ cr.car_type }}</td>
          <td>
            <button class="btn btn-outline-danger btn-sm mx-1" @click="deleteCar(cr)">x</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: "App",
  // components: {
  //   HelloWorld,
  // },
  data() {
    return {
      //msg: "Hello Babeee <3"
      new_car: {
        id: "",
        name: "",
        age: "",
        type: "",
      },
      cars: [],
    };
  },
  async created() {
    await this.getCars();
  },
  methods: {
    async getCars() {
      var response = await fetch("http://127.0.0.1:8000/api/cars/");
      this.cars = await response.json();
    },
    async createCar() {
      await this.getCars();
      await fetch("http://127.0.0.1:8000/api/cars/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.new_car),
      });
      await this.getCars();
      this.new_car = {};
    },
    async updateCar() {
      await this.getCars();
      await fetch(`http://127.0.0.1:8000/api/cars/${this.new_car.id}/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.new_car),
      });
      await this.getCars();
      this.new_car = {};
    },
    submitForm() {
      if (this.new_car.id === undefined) {
        this.createCar();
      } else {
        this.updateCar();
      }
    },
    async deleteCar(deletedCar) {
      await this.getCars();
      await fetch(`http://127.0.0.1:8000/api/cars/${deletedCar.id}/`, {
        method: "delete",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.new_car),
      });
      await this.getCars();
      this.new_car = {};
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>