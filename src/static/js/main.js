// shown: 先出模态框；show:先出alert
$(function() {
    $('#myModal').on('shown.bs.modal', function() {
        reset_form();

        $("input[name='multiple']:checked").each(function() {
            let term = $(this).val();

            // 如果是spring term的课，判断form里的单元格是否为空
            if (term ==="spring") {
                if ( $("tr#course1").children("td:eq(0)").text()==="" ) {
                    $("tr#course1").children("td:eq(0)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course2").children("td:eq(0)").text()==="" ) {
                    $("tr#course2").children("td:eq(0)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course3").children("td:eq(0)").text()==="" ) {
                    $("tr#course3").children("td:eq(0)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course4").children("td:eq(0)").text()==="" ) {
                    $("tr#course4").children("td:eq(0)").text( $(this).next("label").text() );
                }

            }
            if (term ==="fall") {

                if ( $("tr#course1").children("td:eq(1)").text()==="" ) {
                    $("tr#course1").children("td:eq(1)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course2").children("td:eq(1)").text()==="" ) {
                    $("tr#course2").children("td:eq(1)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course3").children("td:eq(1)").text()==="" ) {
                    $("tr#course3").children("td:eq(1)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course4").children("td:eq(1)").text()==="" ) {
                    $("tr#course4").children("td:eq(1)").text( $(this).next("label").text() );
                }

            }
            if (term ==="winter") {

                if ( $("tr#course1").children("td:eq(2)").text()==="" ) {
                    $("tr#course1").children("td:eq(2)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course2").children("td:eq(2)").text()==="" ) {
                    $("tr#course2").children("td:eq(2)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course3").children("td:eq(2)").text()==="" ) {
                    $("tr#course3").children("td:eq(2)").text( $(this).next("label").text() );
                }
                else if ( $("tr#course4").children("td:eq(2)").text()==="" ) {
                    $("tr#course4").children("td:eq(2)").text( $(this).next("label").text() );
                }

            }

            // calculate total credit
            let credit = $("input[name='multiple']:checked").length * 4
            $("h6#credit").text( "Total credit: " + credit );


	    });
    })
});

function reset_form() {
    $("tr#course1").children("td:eq(0)").text("");
    $("tr#course1").children("td:eq(1)").text("");
    $("tr#course1").children("td:eq(2)").text("");

    $("tr#course2").children("td:eq(0)").text("");
    $("tr#course2").children("td:eq(1)").text("");
    $("tr#course2").children("td:eq(2)").text("");

    $("tr#course3").children("td:eq(0)").text("");
    $("tr#course3").children("td:eq(1)").text("");
    $("tr#course3").children("td:eq(2)").text("");

    $("h6#credit").text( "Total credit: " + 0 );
}

function check() {
    //判断春节，最多选4门课，超过4门课，设置复选框为不可选状态
    if ( $("input[value='spring']:checked").length === 4 ) {
        $("input[value='spring']:not(:checked)").each(function () {
            $("input[value='spring']:not(:checked)").attr("disabled", "disabled")
        })
    }
    else {
        $("input[value='spring']:not(:checked)").each(function () {
            $("input[value='spring']:not(:checked)").removeAttr("disabled")
        })
    }

    if ( $("input[value='fall']:checked").length === 4 ) {
        $("input[value='fall']:not(:checked)").each(function () {
            $("input[value='fall']:not(:checked)").attr("disabled", "disabled")
        })
    }
    else {
        $("input[value='fall']:not(:checked)").each(function () {
            $("input[value='fall']:not(:checked)").removeAttr("disabled")
        })
    }

    if ( $("input[value='winter']:checked").length === 4 ) {
        $("input[value='winter']:not(:checked)").each(function () {
            $("input[value='winter']:not(:checked)").attr("disabled", "disabled")
        })
    }
    else {
        $("input[value='winter']:not(:checked)").each(function () {
            $("input[value='winter']:not(:checked)").removeAttr("disabled")
        })
    }

}









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



