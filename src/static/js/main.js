console.log("hello".length);

console.log("hello".charAt(0));

console.log("hello, world".replace("hello", "goodbye"));

console.log("hello, world".toUpperCase());

var name = 'Hao2';
console.log(name);

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

var a = [];
a[0] = "dog";
a[2] = "cat";

for (let i = 0; i < a.length; i++) {
    console.log(a[i]);
}

//不会输出空的
for (let i in a) {
    console.log(a[i]);
}

b = ["dog", "cat", "sheep"];
b.pop();
console.log(b);
b.reverse();
console.log(b);
b.push("fish");
console.log(b);
b.unshift("lion");
console.log(b);
b.shift();
console.log(b);
