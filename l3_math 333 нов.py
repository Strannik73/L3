from math import pi, sqrt
r = input('радиус окружности в сантиметрах')


   

cr =  (int(r) * 2 * pi)
print(str(cr) + ' длина окружности в сантиметрах') 
cm = cr / 100
print(str(cm) + ' длина окружности в метрах')

so = (pi*int(r)**2)
print(str(so) + ' площадь окружности в сантиметрах')
som = so / 10000
print(str(som) + ' площадь окружности в метрах')

avk = (int(r)*sqrt(2))
print(str(avk) + ' длина квадрата вписанного в окружность в сантиметрах' )
avt = (int(r)*sqrt(3))
print(str(avt) + ' длина треугольника вписанного в окружность в сантиметрах' )
 
aok = (2*int(r))
print(str(aok) + ' длина квадрата около которого описана окружность ')
aot = (2*int(r)*sqrt(3))
print(str(aot) + ' площадь треугольника ')
    
aw = (2*int(r))*(sqrt(2)- 1)
print(str(aw) + " длина описаного восьмиугольника")






<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="style.css" rel="stylesheet" type="text/css">
    <!-- <link rel="stylesheet" href=""> -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap" rel="stylesheet">
</head>
<body>
    <header>
        <div class="header-flex">
            <div class="header-left">
                <img srt="assets/logo.svg" alt="логотип компании">
                <ul class="link-list">
                    <li><a href="#">Features</a></li>
                    <li><a href="#">Prising</a></li>
                    <li><a href="#">Integration</a></li>
                    <li><a href="#">learn</a></li>
                </ul>
                <div>
                    <button>Sing in</button>
                    <button>Book a demo</button>
                </div>
            </div>    
        </div>

</body>
</html







.header-flex {
    display: flex;
    justify-content: space-between;
}

.header-left {
    display: flex;
}
.link-list {
    display: flex;
}
li {
    list-style-type: none;
    margin-right: 24px ;
}
a {
    text-decoration: none;
    color: #33383F;
    font-size: 15px;
}

.sing-in {
    font-size: 15px;
    color:#0070A0;
    border: none;
    background: none;
}
.demo {
    color: #ffffff;
    padding: 6px 20px;
    background-color: #0070A0;
    border: none;
    margin-left: 21px;
}
