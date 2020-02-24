function Submit() {
    //document.querySelector("li") 找到第一个返回给你
    alert();
    //通过class选所有元素
    document.querySelectorAll("input.form-check-input")
    //通过tag选: ("li")
    //通过特定id下的li选： （"#id li"）


    document.querySelector("#confirm").addEventListener("click", function () {
        alert();
    });

    document.querySelector("#credit").addEventListener()
}


<<<<<<< HEAD

$(document).ready(function(){
  $("button").click(function(){
    $("p").hide();
  });
});

=======
>>>>>>> 7ec0df9e379cef1a0a05c3aebddd9fda5269a02c
//JS回顾：
//字符串
console.log("hello".length);
console.log("hello".charAt(0));
console.log("hello, world".replace("hello", "goodbye"));
console.log("hello, world".toUpperCase());

var name = 'Hao2';
console.log(name);

//字典
obj = {
    name: "Simon",
    age: "20",
    email: "simon@gmail.com",
    contact: {
        phone: "1234567",
        Telegram: "@Simon"
    }
};

console.log(obj);
console.log(obj.contact.phone);

//循环
var a = [];
a[0] = "dog";
a[2] = "cat";

//a[1]没有定义，会空出一个
for (let i = 0; i < a.length; i++) {
    console.log(a[i]);
}

//这种方式就不会输出空的
for (let i in a) {
    console.log(a[i]);
}


//list操作
b = ["dog", "cat", "sheep"];
b.pop(); //pop 最后一个
console.log(b);
b.reverse();
console.log(b);
b.push("fish"); //push 放到最后一个
console.log(b);
b.unshift("lion");// 放到前面
console.log(b);
b.shift();//删前面
console.log(b);

//函数
let c = 1
function add(x) {
    c += x
}
add(4);
console.log(c);

//带参数的函数
function add2() {
    let sum = 0;
    for (let i = 0, j = arguments.length; i < j; i++) {
        sum += arguments[i];
    }
    return sum;
}
let sum = add2(1, 2, 8, 9);
console.log(sum);

//闭包
function makeAdder(a) {
    return function (b) {
        return a + b;
    }
}

var x = makeAdder(5);

//6传入到里面的返回函数
var sum2 = x(6);
console.log(sum2);



