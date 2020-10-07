Vue.component("dot", {
  template: "#dot-template",
  data: function () {
    return {
      isActive: false,
      message: "Hello",
    };
  },
});

new Vue({
  el: "#app",
  data: {
    count: 100,
  },
  mounted() {
    childrenComp = this.$children;
    let i;
    for (i = 0; i < this.count; i++) {
      var compareValue = i + 1;
      if (compareValue % 3 === 0) {
        if (compareValue % 5 === 0) {
          childrenComp[i].message = "FizzBuzz";
          childrenComp[i].isActive = true;
        } else {
          childrenComp[i].message = "Fizz";
          childrenComp[i].isActive = true;
        }
      } else if (compareValue % 5 === 0) {
        childrenComp[i].message = "Buzz";
        childrenComp[i].isActive = true;
      } else {
        childrenComp[i].message = String(compareValue);
        childrenComp[i].isActive = true;
      }
    }
  },
});
