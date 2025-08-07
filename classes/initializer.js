class Human {
  constructor(gender, name) {
    this.gender = gender;
    this.name = name;

    if (gender === "Male") {
      this.ribs = 24;
      this.curse = "Suffer";
    } else {
      this.ribs = 23;
      this.curse = "Pain";
    }
  }

  print_self() {
    console.log("----------------------");
    console.log("name", self.name);
    console.log("gender", self.gender);
    console.log("ribs", self.ribs);
    console.log("curse", self.curse);
    console.log("---------------------");
  }
}

let adam = new Human("Male", "Adam");
adam.print_self();

let eve = new Human("Female", "Adam");
eve.print_self();
