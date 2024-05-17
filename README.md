Para rodar o projeto é necessário ter o Python, pip e ROS instalados no seu computador.


Rode Git Clone https://github.com/pedrocruz2/prova-m6-s2/

rode cd prova-m6-s2

rode pip install -r requirements.txt

rode ros2 run turtlesim turtlesim_node

rode python/python3 publisher.py

A partir disso você pode controlar a tartaruga utilizando python/python3 cli.py --vx "valor em float de vx", --vy "valor em float de vy", --vtheta "valor em float de vtheta", --t "valor em float de t"

sendo: vx a velocidade em x da tartaruga, vy a velocidade em y da tartaruga, vtheta a velocidade angular da tartaruga e t o tempo em que ela se movimentará nas velocidades definidas
