from django.http import HttpResponse


def about(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>About Kami</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 20px;
            }
            .header {
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                text-align: center;
                padding: 20px 0;
                border-radius: 5px;
            }
            h1 {
                margin: 0;
            }
            .nav {
                display: flex;
                justify-content: center;
                background-color: #f1f1f1;
                padding: 10px 0;
                margin: 20px 0;
                border-radius: 5px;
            }
            .nav a {
                color: #333;
                text-decoration: none;
                padding: 10px 15px;
                margin: 0 5px;
                border-radius: 4px;
            }
            .nav a:hover {
                background-color: #ddd;
            }
            .content {
                text-align: center;
                margin-top: 40px;
                padding: 20px;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                padding: 15px;
                background-color: #333;
                color: white;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Tentang Kami</h1>
            </div>
    <div class="nav">
        <a href="/">Home</a>
        <a href="/produk/">Produk</a>
        <a href="/kontak/">Kontak</a>
        <a href="/about/">About</a>  
    </div>


            <div class="content">
                <h2>Selamat Datang di Katalog Produk Premium</h2>
                <p>Kami adalah perusahaan yang berdedikasi menyediakan produk berkualitas dengan harga terbaik. 
                Fokus kami adalah kepuasan pelanggan melalui layanan yang profesional dan produk terpercaya.</p>
                <p>Didirikan tahun 2025, kami terus berkembang dan berinovasi untuk melayani kebutuhan Anda.</p>
            </div>

            <div class="footer">
                <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
            </div>
        </div>
    </body>
    </html>
    """)

def homepage(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Katalog Produk</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 20px;
            }
            .header {
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                text-align: center;
                padding: 20px 0;
                border-radius: 5px;
            }
            h1 {
                margin: 0;
            }
            .nav {
                display: flex;
                justify-content: center;
                background-color: #f1f1f1;
                padding: 10px 0;
                margin: 20px 0;
                border-radius: 5px;
            }
            .nav a {
                color: #333;
                text-decoration: none;
                padding: 10px 15px;
                margin: 0 5px;
                border-radius: 4px;
            }
            .nav a:hover {
                background-color: #ddd;
            }
            .hero {
                text-align: center;
                padding: 60px 20px;
                background-color: #e9ecef;
                border-radius: 8px;
                margin-bottom: 30px;
            }
            .button {
                display: inline-block;
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                text-decoration: none;
                border-radius: 4px;
                margin: 10px 0;
            }
            .button:hover {
                background-color: #45a049;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                padding: 15px;
                background-color: #333;
                color: white;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Katalog Produk Premium</h1>
            </div>
            
                    <div class="nav">
            <a href="/">Home</a>
            <a href="/produk/">Produk</a>
            <a href="/kontak/">Kontak</a>
            <a href="/about/">About</a>  
        </div>

            
            <div class="hero">
                <h2>Temukan Produk Berkualitas</h2>
                <p>Koleksi produk terbaik dengan kualitas premium dan harga bersaing.</p>
                <a href="/produk/" class="button">Lihat Produk</a>
            </div>
            
            <div class="footer">
                <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
            </div>
        </div>
    </body>
    </html>
    """)

def daftar_produk(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Daftar Produk</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 20px;
            }
            .header {
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                text-align: center;
                padding: 20px 0;
                border-radius: 5px;
            }
            h1 {
                margin: 0;
            }
            .nav {
                display: flex;
                justify-content: center;
                background-color: #f1f1f1;
                padding: 10px 0;
                margin: 20px 0;
                border-radius: 5px;
            }
            .nav a {
                color: #333;
                text-decoration: none;
                padding: 10px 15px;
                margin: 0 5px;
                border-radius: 4px;
            }
            .nav a:hover {
                background-color: #ddd;
            }
            .product-grid {
                display: grid;
                grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .product-card {
                background-color: white;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
            .product-img {
                height: 200px;
                background-color: #f5f5f5;
                display: flex;
                align-items: center;
                justify-content: center;
                color: #aaa;
            }
            .product-info {
                padding: 15px;
            }
            .product-name {
                margin: 0 0 10px;
                color: #333;
            }
            .product-price {
                color: #e91e63;
                font-weight: bold;
                margin-bottom: 15px;
            }
            .view-btn {
                display: inline-block;
                background-color: #2575fc;
                color: white;
                padding: 8px 15px;
                text-decoration: none;
                border-radius: 4px;
            }
            .view-btn:hover {
                background-color: #1a5fc8;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                padding: 15px;
                background-color: #333;
                color: white;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Daftar Produk</h1>
            </div>
            
           <div class="nav">
    <a href="/">Home</a>
    <a href="/produk/">Produk</a>
    <a href="/kontak/">Kontak</a>
    <a href="/about/">About</a>  
</div>

            <p>Berikut adalah produk-produk berkualitas yang kami tawarkan:</p>
            
            <div class="product-grid">
                <div class="product-card">
                    <img style="margin-left: 65px;" src="https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcRv_7XD6Sl1W__MoN3XEy7M-pdvGYtZjWm2fiRyTiiD7bUCML7vj74NsXztNrXoRae2_dNTccO4NEZTaulmu4CyBceb6X0VoHvEQJ0T8G7YzktAQZJDGTENZw" class="product-img" alt="Laptop HP Pavilion">
                    <div class="product-info">
                        <h3 class="product-name">Laptop HP Pavilion</h3>
                        <p class="product-price">Rp12.000.000</p>
                        <a href="/produk/1/" class="view-btn">Lihat Detail</a>
                    </div>
                </div>
                
                <div class="product-card">
                   <img style="margin-left: 95px;" src="https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQ8rL6GVF4BhbGAnYypW0WVLTZ5tLnAgfcp0JdfA-Q4kpK2M6TN35zCoymmICrkkrVpjkFXDzVslUzBm5FfPmYBTlhrS1f5YbLHz19vSQJWkh128HizgyeaAsx8LUDnuz8GZrhi-AatVg&usqp=CAc" class="product-img" alt="Laptop HP Pavilion">
                  <div class="product-info">
                        <h3 class="product-name">Smartphone Samsung Galaxy</h3>
                        <p class="product-price">Rp8.500.000</p>
                        <a href="/produk/2/" class="view-btn">Lihat Detail</a>
                    </div>
                </div>
                
                <div class="product-card">
                    <img style="margin-left: 65px;" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMSEhUTEhMVFRIXGRcZFxYXFxcYFRcYGhUWFxgaFx0YHiggGBonHRgXITEhJSkrLi4uFx8zODMtNygtLisBCgoKDg0OFRAPFysdFR0tKy0tKy0tLi0tLS0rKy0rLS4tLS0tLS0rLS03LS4tLS0tLTcrKy0tLSsrNzAtLSstLf/AABEIANMA7wMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAAAwQFBgcCCAH/xABMEAACAAMEBQgHBAcGBAcAAAABAgADEQQSITEFQVFhcQYHEyIygZGhI0JSscHR8BRicuEzY3OCkrPCFSQloqPxNEPD0xc1U1SDk7L/xAAXAQEBAQEAAAAAAAAAAAAAAAAAAQID/8QAHBEBAQEAAwEBAQAAAAAAAAAAAAERAhIhYQMx/9oADAMBAAIRAxEAPwDcYIIIAggggCCCCAIIIIAggggCCCCAIIIb263S5KF50xZaDNmIUecA4gijaS51LBLDCWzznFaBUYKTq6zACm8VihW3nGnTwwmS5ZqTQVmBVUjs0DANxOde6Lia2qRpWQ79Gk2Wz49UMCcMThuh5GEcmeWsyyLRZEl3NazWBEwgsSFwwCjIAUGG2pi0SOdV/Wsqk/dmEDzWGGtPjlJgORB4GsZPpznDM1KGSyJrAmHrGuXVUFicgBFf5H8p7SukZUyaoSy9dGlrT0YYYM4GAIIWoqWzzhhreoIbWW3ypv6OYj/hYGHMRRBBBAEEEEAQQQQBBBBAEEEEAQQQQBBBBAEEEEAQQjarVLlremOqKM2Zgo8TEFP5cWFezPE39irTa8CgIPjAWOCKk3OBZ8aS510EAs4lygCdXpnU17ob2/nPsElwjOxLAkXBeWoBIW8MKkqRxzpAP+XHLGVo6UCRfnvXo5Vc/vNsQHX3CMG03pqfbZnSWiYztqGSINiLkB57SYltKWCdbZr2qfMAeYagEnqr6qLgaKoPvOZMNf7EVc5nkflGpGaipUj6wh7Js0LNZlX1vIxyLSq6/KKHMqyCHsqxbzDCVpiUM2A41+AMP5GnrLhWcgGuhrTeQOtTu40gHf8AZ4alScNmBO6oFfCG2lbfJsq0NL1MEWnnTKGOneVyJVLNidcwjD92KLabQzksxJJzJiB/pDlJPmPeVzLoarcJUjZQjGsbvzQ8tzpCQZU9gbXJAvHCsyXksym2uDb6HXHm5oneQmnzYbdItFSEDBZu+U5AfjTBuKiJVj1rBHEqYGUMpBUgEEYggioI2iO4iiCCCAIIIIAggggCCCCAIIIIAgghrpLSUmzoZk+YkqWM2dgo89e6AdRBcure9nsFomyjdmKnVbWKkCo34xSeUfPRZ5fVsctrQ3ttWXKHCovN4DjGdae5zdI2tGlP0Ykvg0tJdKrsvElvCLiELHpyczBpjGaRrnEzadaUCQHqAaTDjuEI6Z5QWlVuiYyBROK3SRRlmXbwINb1ygrvMNLBPX1pMw1BGGw3K57kA7zDu3Vm1u2e7UTMTUn0hqSMgCKUEVFdtekprM3pDiXGBwoyg+GEPeSlnM2debHGtTiduveTBatHviSt2pByAxAujhhDTR2nGsrm6isN9R4UgN00HZ5f2S0z+jWbNlYKjC8qrQG+V1+t/DEZIsMu1KJpXo5UsenmgpJlkk4BAQVBGVdewYRnVh5w3lteVHlttR6YbDhiNxh3J5yJgLENOBYUbsspGdKHDWchrMBolq5DSQ9oUzZoEoSWQgIbyzTQVyqQQw1as8oY2jm8QTWDTnEnpkkIwClrzSw158hdvELQYmuqKbM5yp5rWdMNQgNUUkiW15KmlTQ++EzzlWisxjMDdIyOweWCt9Ltx1GF1hdXL2RAWqTzYhqB7Vdcz2kECUSKqhfqm9rArU0pGeW6x/Z7TNk1DdHMdK0pW6xWtNWUSdk5y7VKChZisUmvOBmSyzGY6urFjUVFHbDVhsitWzS/SzXmueu7M7UFBVmLGg1CpMA+t9luUwqvw2cIj7RMl1N2v1xoffElP0xIaWFLNeH3T84jbqvipDayNfGhgG5OqPsuXjt3fP5R9ZYltD2YMaGA1jme5c3FWw2s0UYSJhwA2Sm2fdPdsrscec7NokEYCLxyc5ZT7MBLngzpQwBJ9Io3E9ocfGJYsrVIIidFcpLNaMJc0XvYbqv4HPurEtEUQQQQBBBBAEEEEAQx0zpeRZJZm2iYsuWMKtrOoKBizbhjD6PPfO5p77XpDoUasmy1QbDNJ9Ie7BP3TtgJvlXzqWmcej0cjSpdcZ7KpmMPuI2CbanHcIp1qNrnm9MWbNauDTWR2rQioDNRKg9lQBHFnYIpY5KK+EOtCvaLU4Cm4pyC08zrjWMoWfoecMfs5phWgUYDV1SaDeMY6s+hyuM1wm4Z+cW60FrPbDZWmdI3RiZWgqlSBQkZ1rXIUwzrhmnKTSpmT5l1uoGouygw8IC+WUSpZS5Mvo23MGJ8WIUjGLDb2UjE0rGw2DSgaUDX1R7oCtcpVxCjMmnzirT9G/XfFnnTelnO2pcBxP5V8YYW2x3mvVp3cRUY4GhO0RRXJmjobvYSItBkFq0GAzJwUcScBDGdNkr2poY5UUE8cQDEwV9pDDWY6FlmFC47INDjEvJRZjTLitcloXdruS1UVo0xdbAbTqEMJloSoCsbp7VVIpsFAxvasYzfjfHPexgax8umHwlV7DI2OArdY9zcIJIQTAs28qhhfAAvXai9SppWlYrJkJcKSCUYMuBBqImOUC2bp2+x3/s5pcv1qcOtS8K0BwxxwiNKQD+2qpuugori8B7LDB17j5EQ6sYwBGB2iGllxRk2dccQKN5Y/uw+0VnSKiZsHKGbKIDAOu/BvERZrDyos0wUbqHYww8RhFJtkmkR7OQcu+o3/XfAaHp2TflN0DhXPZYUI4V1VyrqiN5Hc4WkrI3QspnSpQZpqzWJZZdRUq5qRQkAZg1ApFYs1rdeySPdDg6SmLeYBTeVkNRUXWpXhlAejOQ/KkaRkNOCdGVdkKXrxAHZJwFKg+RixR5y5IcuUsNokXBWU1yXPYrdpLF7sgZkO7TCca9amdB6MBrlErT7BBBEBBBBAV7l/p02GwT7QtOkC3ZdcukchE8Ca90eabBImHrXWcnEsAWJJxJNNdY3bnrmEWGXTPp1/lzIwv7c8vJVrtBuH/KQe6LEp5PDMhWjKcM1bUa0O7CJbRelJtnT0Eq7M1tMN5F3iigt30iAPKiauZmU3TWp5nj4RH6S070ilWMw11F6jziocaW0z0fS3Zpm2mcfTTznwWmA2YZeFKuBHRYahHQc5DAbojT5LU1iz6L0i6oVxPDH3RWllw/0fo2Y+IJVDhXEk7QgGLncO+ESrXo40khjm1XPfl5AQ3tFrxoq1NdeHlmYlhoqcwHo1lrqM40oP2a1PjH0aOuijTAx2qjKMwaUDrsPiY0itT7PMm0v3mABFAvVH4RkDvplr1wJYWFaFxeoMMKsuVAAKgdw3mLDWWuctG4q/wB79bvH8I314FosxwMsyzQdZGfUBWoLHPPjuwiCBfRt6rGYx6wap61ZmXFzwFNUfF0K6k3LjHEEFVLG9tB7OI4+NItgs6M1bPM6VAtKTVUstcxVDeUZUPltazkQCjKZewE3pDttZwLwrsYHeTqCnWjRuIa4FUdoKWusQcQC1aEwTdHqsw0BKKQSbrFQCcLwNCuyhIrqMWu01U0cg3a+kbsi8P8AkgGjasQab9UNQ9zEXgDTq4dJMqKG8MeruIoRqhhpja5HSIBeRZCk9EFLMpJGNSespGOBxx1gRBWiU0o9bEHIw+tSvKYstCp7aDJak4GmApuyhva5xmUJNV1avHfvgPtjnhWVtQOPDI+VYkrOtyZTYad1cD4RAEFeBifszXkRt108U6v/AObvjCCZ0iOyAMwWO5RQeNSPOE25PvXrNKWidI4M0lpcu4HvTFSWTky4CpqwwhzLF4psZGTHaCrDhhe8IsVol2tqKZcuYLiySv2qYZcyW0uXLvKgwQAPKJcYgnKhIgICRyeKyzNa6ZZFZbILRMDgqGqbkv0YxpV7uIbYTDFpFKEgBDhX2TqB3HbFx0dZpyMrqlnS4qJLKvPe7LFWVxj6VS071wTVuzQGI3SFkEu5LqCKqQwyKhQ4OONKUzgKDbZN12XMfAiPUPNrpA2jRdkmMSWMoKxOZKEyyfFY816dHpK7RHoLmYeuiLPuM0f6zxKsXeCCCIoggggM/wCepa2GXr9On8ubGNNY66sxhh354466Z03YxsfPU9LJJG2ePKVMjK5Bw+gCKjPD46841GarVqsFBlqr5cPLGK9a1oxEXu3ZHbj7jWuzPLzijaQPXNMvrZEqw2hSXCcWzkNyaNqe+6kyVOWXSMMSK6lGFTvpriKdclOSZngTZvVlagRi3drGWsDbsN0lvKk1EhMcjMwGA1GYaCgqequA2RC6a09dcyUuTGXAKh9Ag/WGgvbAq4YetEW9mmTaPPZnWt3EUlKaA0CDDskGhzGUaZTFp00hwE1SdksFzv6w+UR862hshMPG7/24kpWjZEtaTWN6h6qlSAwLAYL6hF1gajXwhsbbZUmTKlbhUhAxSqsbprQnIUYA50I1xRETnPs0+vwrDNw3st3Y+Wsd8WZrZZpgmGXdDFgUCsrACpqMCLvVpqOI3mFW0VKMnpBMHSVAKEgGvWJoajC6F241EBShNYG8pxGtSQ47sxnmIfyOUJOE3rD2gBe33hk/keMSmltBsp9KpqCQJi4NUZ0YCjUio22Xda6QynaQMd4pgw4UiCaa3FKXKMlb1wmqVyvJ7DZ/ER9lWsEVViPaY9uvsgavrGK8s0rgcj4HeD8Y7SeVIIp8DxhomplAMqL7Gt8cC276ERU2z9GSaVVhljRW38NnjD2TNqKgke07dquwb/PgI+lQRQ4IctpOo93hxgIoDbiDgfmOESWiKhZks5qytxB6pI3djxhuJJDXTn8of2GTRhvVpfddLp5qR4QE5o9S0sUFSjq1Nq0KOP4WaJC3cq7QD1UVaFbpKsWAXo8LzMSwbo0reqcMxEJo7TMuQTfJx2QpNtkufUyzU7NcUSdh5S2gmgRKVFBdAAUBQEHWrcF1TTOozh7amd/STCL1KBVyUUp7qADUNsQujhjEzaW6kBTdOdscPjG98yL10TK/HOH+q0YLpvtDv98bxzG/+Uyv2k7+a0Zqxf4IIIiiCCCAzjnu/wCGs/7atdlJbxlUt8Ka+BPDDMY93GNU58P+Gs/7b/pPGSq+A15b/ADDZGozXNsPVOzHPLdl7teOB10i3ds/R798XC1E0PwBwwI3a8MMa17qda+0YlWOtHWNp0xZa5sacNp8Iv2l9JdDLWxWXqmgDuNQzIqN5JO0nfFb5LASlmWg5gXU4nM+4d8THJfR/SvemesQW241uL3neMzrpFhT7QuikRA75ZgVUlsG7Vc2JC0X7wJFKwtbtK3xS8EkJQVbsilKDq4u2xRgMsBjEfpG1AHopbN0dS2JrdWgFcABeIoK02Qvo2woUFqtC3pIJWzyKkCYwzZiDUIp7RzY4bYuEmmoDTVLy5YEkGhnWkgJ3JUIOHWaGM+2SkznlzslywqdxIWo7o605bJk5qzDWmCqBREHsoowUcIr9oSJda64fzNISm37L6g+YxhxZNIlTWW5Wm8ugPCt5O4xXiuyPisQajA+cTWcaZo3lAsyku0IDerRu0SSalkfNjXMdrjiC30/oiWTdvBwQGVhgwrlXUG8iCNuFMsVs9Uitc1yDUyI9h9hH5G3aDt+IBusWBCO1MR2WqD1Q61oa4Ct4aoqKba7MZbGW+Wat8R5imqphBM7p8dVfkYu3KXRAaqBlZ1oQVNQGOa11+yTlkdUUmYKiusYHb38MoindiehoRux1HIE+7wiRl41xqdbHLu+vCIwmqrM29R+IGfeuPFTEghyOZpl6opgSduNYsR1P7KsMxu1AZniK/ww90VLZ7zgVRDLDHDAsSyb8ejcf7w1rUMKkjBjQYE68DkArMKxxoS3PLfo1ICTWliYKZ3HqtDqxMAqLbLIIlrKbUZcwG+xGBKOBTHUpiPNKiZLqmOWwjUYYJmeJ98TUihCsc5kuYG/HKxVu9SB3mAsejZvSKszJsn2V1HviQtb9WkQnJ5sH2dXxxiWtZwiiq6aPWHf8I3vmOH+ESvxzv5rRgWmT1h3xv8AzIj/AAiT+Kd/OeM1YvkEEERRBBBAZvz4j+6yP2//AEpkZHXxI26s9fwpGwc9y/3OSdk9f5cyMcB2U/315VOv57dRmkbVShpxz3ALmSKZahnFQta0aLbO7OumJoa+J1cdsVS2L1jCrE06UkSpXtEV78T7z4RbbFMEqzMareY0PaDqtK6zS6VGBAFakEmlIq041mSdl0keH5xKaWtbCyuCagLQYAZ0TEgVNAaCtaQQ10VIa0TEStGnNifZUE+4Bm8IsGmbWJjEqKS1ASWupZa4KPid5MQnJpws0n2JT04lQn9Rh1aJkXfZHf8AOZLUbbR8Ij51l1nL37PHyh9MfHx90TVl0K9pvdGKhc+6lfKM/rznHNWce2qvK0WSt9iqJqJ1+fvhraLHQVVgw2j6xi2cpLIkvoekxl1UOFPWC169NhoDDmXoqy/2bMnK/XDejB7Xaotd93OM9559cJ7LYz0CJ3RM0t1QesxFCchNANxuDiqHbU7BEROXHvPv/wB4XsJ7QGBKmnFesPcfGNDQ5NqE+zAl0RVxC+szEUowzDYEXhh1DUVxioaVsHpCdT1/iAx8Rj3GLNoG2OJk0SkDM4DqCt6gmSxMZlG49J3VhrpWQVDAqbyEMV14EBhxusYqKnotLyzZWsoXH45XWp3rfHfC9meqDXlhtNKY7urXvjuw0S2pXIuoPCYAD5OYbWIUR1OYu+8gwU9DVrmxutlhSgJpvAz4YcWuj/0yfir4Y/CFwa540BzwAw1bTCdiIBB3V+PzgiOlDPiffDpbRkBjQFV3lj1j8IUl6PM016qDcCe/jElZrCkvEYt7R+EBI6Hl3FAOZxMSVrbCI+xtDy1HCKKzpc9YcDHoTmXH+EWfjN/nPHnvSvaHD4x6I5mx/g9l3iZ/OmRmrF0gggiKIIIIChc9Muuj1Psz5ZPeHX+qMTw+vMZ4xu3O9LroyaRqeSf9VK+RjBq4A+fidnyjUZpKc3V2U8cse/Hypvis24daLLMypXuqMfnwGoY0iuW3MmFIkpbYyDtQDy/KJbSyVs0wbgfBgfhEBKf0KNrlsR3Vve4mLRIAdCDkwIPAikBD6HnUmn7yMP8AKD44Q4nzog1dpZBPalmhHA/XjEhaZmNR2TiOH1hGb/dd+HLzHEybQxN8nuVDWUv9730+OEVma8NmmROcnOZyO143YmdIaUWeSJta1NCN8NxMAW6pPfESTHSscqxqeeON9pWYanDIQ60WPSLs63kjE+UNANUSuipFQx2i4OLdqnBA3iNsBYtFzWlTJbKaP9nlY565ya/u4QrpKezB5rEluqS1NYIpWmGS+UDrSdO2J0ckcZadf/OzDuhHSH6J/wB0eLqPiY0ivzx/ekpqaV5FflDWU9TMO1v6iYczH9Ozalqf4V+YhjZRReJ9w/OIF5rUB4UFd+NV2ZRyrUHl9d3vhNzeNNQxPE58cKeccF6mgyEBLWJ6CHF+GEp6CF5bQErZGh9aMojLI0SM04RRWtKnrDh8Y9Ic0aXdEWMfcJ8Zjn4x5u0p2hw+MemubNKaKsQ/UIfEV+MZqxZoIIIiiCCCAr/OBZ+k0dal/VM38IvfCPOKnKn5+VY9Vz5KurI4DKwKsDiCCKEHdSPNXL/QczRtpZGQmzOSZEwVoVJqEJyvrlTXQHXFiVBzThu+vHvw8cYK1rEjMtqEf7QwmMDlSKjnRjYtLPrjD8QxHiKiJzQFpwuHNfdqivWazTHakpHcg+opYg6shEva7LOklJzSnllq1VlK1PrAV1HMRIpTlFYqHpR2WoH3HJW+ERNnm09G+Xqts/KLdZJ6zU1FSKEHzBivaV0SZWIBaTt9ZOO7fFsJUfOBBofreNohu0OwSBRhfTUwzHyjkWYN2HB3HA/XdGca7aaR2sOBo2ZXL3/KHMvRwX9IwXcM/P4AwQlY7OXNBTaScFUa2Y6l3+EXHQ8sSl6YLVZVBKUihmTmxUHvAdh6qIBrENLFYAiCZMrKkVFOrWbNOoSUOM19jN1RnhEkzXiGKhAoKy5daiUpxYk+tNbN37hgI1iWkrPJuKFreOJZjmzE1YniSYb6QnABa5VZ2/DKB97kD92HbY4AgE1xOSgCrM24DHwGuK5pa1VqBgHu4HtJKX9GDsLds8RFRGu5un25hp53m+EdKuzgPnCd4do4DJeGs98IzrbqUU3xlXc+ZTqjvMEiGqQurQD1GhzLaI+W8OZcyKiXsjRIzJguxCSJ1IWM9mIVQzMxoqqCzMdQUDEmKGs6zPPnLKlAtMchEAzLMaD58AY9Z6IsIkSJUlcpaIgp91QPhGf81nN19jP2u1gG1sOomYkAihx1zCMCdQwGsnS4zVggggiKIIIIAiO01Ypc+W0qbLSYjZq4DL4HXEjCLLAZTpDmgsLGqLMl7lmGncGrSGdm5o7Ghqelfcz4d90CNcdIbvLgKxYNBJJUJLRZajIKAB5Qhpzk7LtMppUwVByOtTqIi0NLhMyoDzdpnQto0dOKsKocj6rjaNjboeWK3LMGB4g5jiI3PS+hpVoQy5qBlOo+8bDGUcpObibIJmSCXQVOGExR/UI1KmK3M0CrtWSTLc6lxU4V7OruhladCTlJ6STLfgTLbzpDyzWufLo3a1hlN1uIxoe4xM2bliyEGYciCekSlaar1MIIrMrRo/8Aavw+0KB76xJWOzOn6OVZ5P3qGdNHAv1QYl5vK2Swf9DVpZQksDTrFqrldIrTuBNTnHS7ejmku9MOxFZ/cKQC0uSAxdizzTnMc3n4A+qNwpH13xCgFnbsovaY7t20nAQTpTrjPZbKpyv0ee34JSnzYiGy2m+Wk2KU812oHNb7vs6aYKAJ+rSi4GpOUAlpO1qiUJDXu1TszSDginPoVPab1zgMMkOT/JefbnvE0QmrzGBpXgKVP3dmwUrbtAc2syY4m216n/0l8gzDUPZXCNRsGi1lqFVQqjAAYARNXGO2jmlnNj9qU/8AxkDyYwym80lqHZnSjxvj4RvnQiDoREV58fmstwyMk/vMP6YTPNpbx6so8H+Yj0P0A2R8+zjZAeehzcaQ9iX/APZ+UKS+bjSPsShxmflHoRbMNkKrZxsgMJsHNfbnPXmSZY2i858KD3xp/IXkLIsDdIAZs4ihmPSoGxBkg4Zxb5cgQ5SXAOUOGEdQlLFIVgCCCCAIIIIAjkiOoIBJlhJkhxSOSsA0aXHBlw7KxwUgGhlxw0msPCkFyAo2l+byyzmaYqtKmNiWlMVqdrL2SeIivT+bWev6K1gjZNkgnxRl90a3dg6HdAY6nIK3D/nWXj0LE+bQv/4fW18H0gyprWVJVPA3iY1voRsEfBLGyGjK9Hc0tkU3pvSTm1l3IB4haV74uujdAypKhJaKij1VAA8osNNuPvjky4BklnAjvo4c3ILkA26ODo4c3ILm6AbdHAJcObm6PoSAQWXCqS4VCR2FgOFWFQsfQsdAQHwCOoIIAggggCCCCAIIIIAj5SPsEByRHJWFIIBIrHy7CtIKQCVIKQrSCkAldgpCtIKQCVIKQrSCkAldj5dhakFIBG7BdhakFIBK5H0LClIKQHIWPtI6ggPlI+wQQBBBBAEEEEAQQQQBBBBAEEEEAQQQQBBBBAEEEEAQQQQBBBBAEEEEAQQQQBBBBAEEEEAQQQQBBBBAEEEEB//Z" class="product-img" alt="Laptop HP Pavilion">
                  <div class="product-info">
                        <h3 class="product-name">Kamera Canon EOS</h3>
                        <p class="product-price">Rp15.000.000</p>
                        <a href="/produk/3/" class="view-btn">Lihat Detail</a>
                    </div>
                </div>
                
                <div class="product-card">
                      <img style="margin-left: 75px;" src="https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRo3ZN3UL8y3JTe52f0qTEVaW1Jzn2D3ajWYQjxkP-VYuUcVAd8z833NRgehq56PTcUJXDJTXagRCocMXDe3F3LH0QMOg-l8Wz0T7iJdD5H15NDKgVvGq5HtQ" class="product-img" alt="Laptop HP Pavilion">
               
                    <div class="product-info">
                        <h3 class="product-name">Headphone Sony WH-1000XM4</h3>
                        <p class="product-price">Rp4.500.000</p>
                        <a href="/produk/4/" class="view-btn">Lihat Detail</a>
                    </div>
                </div>
                
                <div class="product-card">
                        <img style="margin-left: 75px;" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEhISExIVFRUVFRISFhUXGBUXFRcXFRgYFxUXGxUYHSggGB0mGxUWITEhJSkrLi4uGB8zODMsOCgtLisBCgoKDQ0NFw8PDysZFRk3NysrNystNysrKysrLSsrKystKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABwMEBQYIAgH/xABTEAABAwICBQcFCQsJCQEAAAABAAIDBBEhMQUGEkFxBxMiUWGBkTJCUqGxFDNTYoKSorLRFSNDcnSTwcLS0/AXJTQ2RFRzs+EWJFVldYOjw/EI/8QAFgEBAQEAAAAAAAAAAAAAAAAAAAEC/8QAFhEBAQEAAAAAAAAAAAAAAAAAABEB/9oADAMBAAIRAxEAPwCcEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQERU5JmN8pzRxIHtQVEVm7StMM54h/3GfavrdKU5yniPB7PtQXaLzHI12RB4EH2L0gIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICKlV1LImOkkcGMaC5znGwAGZJUK678pUtQXQ0pdFDkX5SyDjmxvYMTv3hBIusev1FSEs2udlGBjjsbHqc7JvDE9ij/SvKpWSEiIMhb2Dbd85wt4NCjnaXoFBsNVrRWS+XUSns23AfNGCx5rHHNxPerIKoxqC6bUOO8r6+u2c32716rtEVraX3WyBxguby52A8/Zz2L3G1a2C1GUuOJub9atG0x6xlpu2RwPWCQtg0TymVkVhzvOD0ZOl68x4qMxGexe2xP3W8VErozV3lOpJrMn+8PPnE3iPy/N78O1b01wIBBuDiCMiCuP2VEjMwR7PFb5qNyhTUZDHXlgNrxE4t6zGT5J+LkezNFdCorPRGlIamJs0Lw9jsjvBGbSNxGRCvEBERAREQEREBERAREQEREBERAVOpnZGxz3uDWtaXOc42DWgXJJ3CywmsOt9HSHYkkvJYO5pnSeAciRk0cbXsbXUWa8a7e7miISOhgBu5jWl7pCD0dpziywHo2OONzhYMfyh68Pr5ObjJbTMddjcQZCPwjx7G7szjlpwKv8AmqPrqDwMI9t1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" class="product-img" alt="">
                    <div class="product-info">
                        <h3 class="product-name">Smartwatch Apple Watch</h3>
                        <p class="product-price">Rp6.000.000</p>
                        <a href="/produk/5/" class="view-btn">Lihat Detail</a>
                    </div>
                </div>
            </div>
            
            <div class="footer">
                <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
            </div>
        </div>
    </body>
    </html>
    """)

def detail_produk(request, id):
    produk_data = {
        1: {
            "nama": "Laptop HP Pavilion",
            "harga": "Rp12.000.000",
            "deskripsi": "Laptop dengan performa tinggi untuk kebutuhan komputasi sehari-hari. Dilengkapi dengan prosesor Intel Core i7 terbaru, RAM 16GB, dan SSD 512GB.",
            "gambar": "https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcRv_7XD6Sl1W__MoN3XEy7M-pdvGYtZjWm2fiRyTiiD7bUCML7vj74NsXztNrXoRae2_dNTccO4NEZTaulmu4CyBceb6X0VoHvEQJ0T8G7YzktAQZJDGTENZw"
        },
        2: {
            "nama": "Smartphone Samsung Galaxy",
            "harga": "Rp8.500.000",
            "deskripsi": "Smartphone flagship dengan kamera berkualitas tinggi, layar AMOLED 6.7 inch, dan baterai tahan lama.",
            "gambar": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcQ8rL6GVF4BhbGAnYypW0WVLTZ5tLnAgfcp0JdfA-Q4kpK2M6TN35zCoymmICrkkrVpjkFXDzVslUzBm5FfPmYBTlhrS1f5YbLHz19vSQJWkh128HizgyeaAsx8LUDnuz8GZrhi-AatVg&usqp=CAc"
        },
        3: {
            "nama": "Kamera Canon EOS",
            "harga": "Rp15.000.000",
            "deskripsi": "Kamera DSLR profesional dengan sensor full-frame 30MP dan kemampuan video 4K untuk hasil foto dan video berkualitas tinggi.",
            "gambar": "data:image/jpeg;base64,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"
        },
        4: {
            "nama": "Headphone Sony WH-1000XM4",
            "harga": "Rp4.500.000",
            "deskripsi": "Headphone wireless dengan noise cancelling terbaik di kelasnya, kualitas suara premium, dan baterai tahan hingga 30 jam.",
            "gambar": "https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcRo3ZN3UL8y3JTe52f0qTEVaW1Jzn2D3ajWYQjxkP-VYuUcVAd8z833NRgehq56PTcUJXDJTXagRCocMXDe3F3LH0QMOg-l8Wz0T7iJdD5H15NDKgVvGq5HtQ"
        },
        5: {
            "nama": "Smartwatch Apple Watch",
            "harga": "Rp6.000.000",
            "deskripsi": "Smartwatch dengan fitur pemantauan kesehatan lengkap, tahan air, dan terintegrasi sempurna dengan ekosistem Apple.",
            "gambar": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxATEhISExIVFRUVFRISFhUXGBUXFRcXFRgYFxUXGxUYHSggGB0mGxUWITEhJSkrLi4uGB8zODMsOCgtLisBCgoKDQ0NFw8PDysZFRk3NysrNystNysrKysrLSsrKystKysrKysrKysrKysrKysrKysrKysrKysrKysrKysrK//AABEIAOEA4QMBIgACEQEDEQH/xAAcAAEAAQUBAQAAAAAAAAAAAAAABwMEBQYIAgH/xABTEAABAwICBQcFCQsJCQEAAAABAAIDBBEhMQUGEkFxBxMiUWGBkTJCUqGxFDNTYoKSorLRFSNDcnSTwcLS0/AXJTQ2RFRzs+EWJFVldYOjw/EI/8QAFgEBAQEAAAAAAAAAAAAAAAAAAAEC/8QAFhEBAQEAAAAAAAAAAAAAAAAAABEB/9oADAMBAAIRAxEAPwCcEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQERU5JmN8pzRxIHtQVEVm7StMM54h/3GfavrdKU5yniPB7PtQXaLzHI12RB4EH2L0gIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICKlV1LImOkkcGMaC5znGwAGZJUK678pUtQXQ0pdFDkX5SyDjmxvYMTv3hBIusev1FSEs2udlGBjjsbHqc7JvDE9ij/SvKpWSEiIMhb2Dbd85wt4NCjnaXoFBsNVrRWS+XUSns23AfNGCx5rHHNxPerIKoxqC6bUOO8r6+u2c32716rtEVraX3WyBxguby52A8/Zz2L3G1a2C1GUuOJub9atG0x6xlpu2RwPWCQtg0TymVkVhzvOD0ZOl68x4qMxGexe2xP3W8VErozV3lOpJrMn+8PPnE3iPy/N78O1b01wIBBuDiCMiCuP2VEjMwR7PFb5qNyhTUZDHXlgNrxE4t6zGT5J+LkezNFdCorPRGlIamJs0Lw9jsjvBGbSNxGRCvEBERAREQEREBERAREQEREBERAVOpnZGxz3uDWtaXOc42DWgXJJ3CywmsOt9HSHYkkvJYO5pnSeAciRk0cbXsbXUWa8a7e7miISOhgBu5jWl7pCD0dpziywHo2OONzhYMfyh68Pr5ObjJbTMddjcQZCPwjx7G7szjlpwKv8AmqPrqDwMI9t1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"
        }
    }
    
    if id in produk_data:
        produk = produk_data[id]
        return HttpResponse(f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Detail Produk - {produk['nama']}</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                }}
                .container {{
                    max-width: 1100px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: white;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    margin-top: 20px;
                }}
                .header {{
                    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                    color: white;
                    text-align: center;
                    padding: 20px 0;
                    border-radius: 5px;
                }}
                h1 {{
                    margin: 0;
                }}
                .nav {{
                    display: flex;
                    justify-content: center;
                    background-color: #f1f1f1;
                    padding: 10px 0;
                    margin: 20px 0;
                    border-radius: 5px;
                }}
                .nav a {{
                    color: #333;
                    text-decoration: none;
                    padding: 10px 15px;
                    margin: 0 5px;
                    border-radius: 4px;
                }}
                .nav a:hover {{
                    background-color: #ddd;
                }}
                .product-detail {{
                    display: flex;
                    flex-wrap: wrap;
                    margin-top: 30px;
                    gap: 30px;
                }}
                .product-image {{
                    flex: 0 0 40%;
                    height: 350px;
                    background-color: #ffffff;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border-radius: 8px;
                    color: #aaa;
                }}
                .product-info {{
                    flex: 1;
                }}
                .product-name {{
                    font-size: 28px;
                    margin: 0 0 15px;
                    color: #333;
                }}
                .product-price {{
                    font-size: 24px;
                    color: #e91e63;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
                .product-description {{
                    line-height: 1.8;
                    margin-bottom: 30px;
                }}
                .buttons {{
                    display: flex;
                    gap: 15px;
                }}
                .buy-btn {{
                    background-color: #e91e63;
                    color: white;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }}
                .back-btn {{
                    background-color: #f1f1f1;
                    color: #333;
                    border: none;
                    padding: 12px 25px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                    text-decoration: none;
                    display: inline-block;
                }}
                .footer {{
                    text-align: center;
                    margin-top: 30px;
                    padding: 15px;
                    background-color: #333;
                    color: white;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Detail Produk</h1>
                </div>
                
                <div class="nav">
    <a href="/">Home</a>
    <a href="/produk/">Produk</a>
    <a href="/kontak/">Kontak</a>
    <a href="/about/">About</a>  
</div>

             
                <div class="product-detail">
                <div class="product-image">
                     <img src="{produk['gambar']}" alt="Gambar {produk['nama']}" style="max-width: 100%; height: auto; border-radius: 8px;">
                </div>
                    <div class="product-info">
                        <h2 class="product-name">{produk['nama']}</h2>
                        <p class="product-price">{produk['harga']}</p>
                        <div class="product-description">
                            <p>{produk['deskripsi']}</p>
                        </div>
                        <div class="buttons">
                            <button class="buy-btn">Beli Sekarang</button>
                            <a href="/produk/" class="back-btn">Kembali ke Daftar</a>
                        </div>
                    </div>
                </div>
                <div class="footer">
                    <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
                </div>
            </div>
        </body>
        </html>
        """)
    else:
        return HttpResponse("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Produk Tidak Ditemukan</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                }
                .container {
                    max-width: 1100px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: white;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                    border-radius: 8px;
                    margin-top: 20px;
                }
                .header {
                    background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                    color: white;
                    text-align: center;
                    padding: 20px 0;
                    border-radius: 5px;
                }
                h1 {
                    margin: 0;
                }
                .nav {
                    display: flex;
                    justify-content: center;
                    background-color: #f1f1f1;
                    padding: 10px 0;
                    margin: 20px 0;
                    border-radius: 5px;
                }
                .nav a {
                    color: #333;
                    text-decoration: none;
                    padding: 10px 15px;
                    margin: 0 5px;
                    border-radius: 4px;
                }
                .nav a:hover {
                    background-color: #ddd;
                }
                .error-container {
                    text-align: center;
                    padding: 50px 20px;
                }
                .error-icon {
                    font-size: 60px;
                    color: #e91e63;
                    margin-bottom: 20px;
                }
                .button {
                    display: inline-block;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 15px;
                    text-decoration: none;
                    border-radius: 4px;
                    margin: 10px 0;
                }
                .footer {
                    text-align: center;
                    margin-top: 30px;
                    padding: 15px;
                    background-color: #333;
                    color: white;
                    border-radius: 5px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>Produk Tidak Ditemukan</h1>
                </div>
                
               <div class="nav">
    <a href="/">Home</a>
    <a href="/produk/">Produk</a>
    <a href="/kontak/">Kontak</a>
    <a href="/about/">About</a>  
</div>

                
                <div class="error-container">
                    <div class="error-icon">⚠️</div>
                    <h2>Maaf, produk yang Anda cari tidak ditemukan</h2>
                    <p>Produk dengan ID {id} tidak tersedia dalam katalog kami.</p>
                    <a href="/produk/" class="button">Kembali ke Daftar Produk</a>
                </div>
                
                <div class="footer">
                    <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
                </div>
            </div>
        </body>
        </html>
        """)
    


def kontak(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Kontak Kami</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f8f9fa;
            }
            .container {
                max-width: 1100px;
                margin: 0 auto;
                padding: 20px;
                background-color: white;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
                border-radius: 8px;
                margin-top: 20px;
            }
            .header {
                background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
                color: white;
                text-align: center;
                padding: 20px 0;
                border-radius: 5px;
            }
            h1 {
                margin: 0;
            }
            .nav {
                display: flex;
                justify-content: center;
                background-color: #f1f1f1;
                padding: 10px 0;
                margin: 20px 0;
                border-radius: 5px;
            }
            .nav a {
                color: #333;
                text-decoration: none;
                padding: 10px 15px;
                margin: 0 5px;
                border-radius: 4px;
            }
            .nav a:hover {
                background-color: #ddd;
            }
            .contact-container {
                display: flex;
                flex-wrap: wrap;
                gap: 30px;
                margin-top: 30px;
            }
            .contact-info {
                flex: 1;
                min-width: 300px;
            }
            .contact-form {
                flex: 1;
                min-width: 300px;
                background-color: #f8f9fa;
                padding: 25px;
                border-radius: 8px;
            }
            .info-item {
                margin-bottom: 20px;
            }
            .info-item h3 {
                margin-top: 0;
                color: #2575fc;
            }
            .form-group {
                margin-bottom: 15px;
            }
            .form-group label {
                display: block;
                margin-bottom: 5px;
                font-weight: bold;
            }
            .form-control {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            textarea.form-control {
                height: 120px;
            }
            .submit-btn {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 12px 25px;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            .footer {
                text-align: center;
                margin-top: 30px;
                padding: 15px;
                background-color: #333;
                color: white;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Hubungi Kami</h1>
            </div>
            
          <div class="nav">
    <a href="/">Home</a>
    <a href="/produk/">Produk</a>
    <a href="/kontak/">Kontak</a>
    <a href="/about/">About</a>  
</div>

            
            <div class="contact-container">
                <div class="contact-info">
                    <h2>Informasi Kontak</h2>
                    <div class="info-item">
                        <h3>Email</h3>
                        <p>info@katalogproduk.com</p>
                        <p>support@katalogproduk.com</p>
                    </div>
                    
                    <div class="info-item">
                        <h3>Telepon</h3>
                        <p>+62 812 3456 7890</p>
                        <p>+62 21 987 6543</p>
                    </div>
                    
                    <div class="info-item">
                        <h3>Alamat</h3>
                        <p>Jl. Contoh No. 123</p>
                        <p>Jakarta Selatan, 12250</p>
                        <p>Indonesia</p>
                    </div>
                    
                    <div class="info-item">
                        <h3>Jam Operasional</h3>
                        <p>Senin - Jumat: 09:00 - 17:00</p>
                        <p>Sabtu: 09:00 - 14:00</p>
                        <p>Minggu: Tutup</p>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h2>Kirim Pesan</h2>
                    <div class="form-group">
                        <label for="name">Nama</label>
                        <input type="text" id="name" class="form-control" placeholder="Masukkan nama Anda">
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email</label>
                        <input type="email" id="email" class="form-control" placeholder="Masukkan email Anda">
                    </div>
                    
                    <div class="form-group">
                        <label for="subject">Subjek</label>
                        <input type="text" id="subject" class="form-control" placeholder="Subjek pesan">
                    </div>
                    
                    <div class="form-group">
                        <label for="message">Pesan</label>
                        <textarea id="message" class="form-control" placeholder="Tulis pesan Anda di sini"></textarea>
                    </div>
                    
                    <button class="submit-btn">Kirim Pesan</button>
                </div>
            </div>
            
            <div class="footer">
                <p>&copy; 2025 Katalog Produk - Semua hak dilindungi</p>
            </div>
        </div>
    </body>
    </html>
    """)