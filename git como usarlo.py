'''
Working Directory  -- git status
Staging Area       --
Repository         --



git config (configurar una cuenta nueva, user y mail)
git log | git log --oneline (para ver los log del proyecto)

asi se inicia un git repo:

    git init (una sola vez)
    git status (estado de los archivos dentro de un repo local)
    git add . (to2 los archivos) | git add [nombre.extension] -> agregarlo al stage (archivos que git tiene en cuenta para modificaciones)
    git commit -m "comentario del cambio que hice"
    git branch (ver las ramas)
    git checkout -b [RamaNueva] (nueva rama creada)
    git checkout [nombreRama] (nos movemos entre las ramas)
    git branch (chekear que toy en la rama correcta)
    git merge [otraRama] (nombre de la otra rama a unir con la que estoy parado)



git log --graph (para ver las)

git diff (ver modificaciones del proyecto)
git checkout [nombre.extension] (borrar todos los registros de cambios)

git reset --SOFT [N° commit unico] (volver a la version deseada, guardando lo posterios)
git reset --HARD [N° commit unico] (volver a la version deseada, no guardando nada posterior)

git branch --d [rama a borrar] (borar la rama q no uso mas)

https://youtu.be/Q4rQIToSmN4?t=5524



git bash
    git clone url
ir con cd.. a carpeta donde clonar

git log --oneline (ver los logs)

git status
git remote -v
git push origin master

'''