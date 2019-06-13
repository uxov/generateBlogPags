*2019-01-13*

# 利用 Github 自建 Maven 仓库并使用 Gradle 发布 Jar 包

原理：将项目打包成 Jar 发布到本地仓库后，本地仓库与 Github 的 repository 进行同步，然后其他项目就可以通过 Github 的 URL 对 发布 Jar 包进行引用。

## 1、配置要发布 Jar 包项目的 build.gradle 文件：
```
apply plugin: 'java'
apply plugin: "maven-publish"

repositories {
    mavenLocal()
    jcenter()
}

dependencies {
    compile 'junit:junit:+'
    compile 'com.google.code.gson:gson:+'
}


//publish jar setting,use 'gradle publish' command
//package source files
task sourceJar(type: Jar) {
    from sourceSets.main.allJava
    classifier "sources"
}

publishing {
    publications {
        maven(MavenPublication) {
            from components.java

            artifact sourceJar

            groupId 'io.github.username.jlib'
            artifactId 'util'
            version '0.1'
        }
    }

    repositories {
        //mavenLocal()
        maven { url 'file:///home/mike/maven-repo' }    //local repository
    }
}
```

## 2、在本地新建一个 maven-repo 目录，如 /home/mike/maven-repo ，作为与 Github 同步的本地仓库。

## 3、在命令行里进入要发布 Jar 包项目的目录里，运行发布的命令：
```shell
gradle clean
gradle build
gradle publish
```

## 4、登录 Github 新建一个 repository 并与本地的仓库 maven-repo 进行同步。   

## 5、在其他的项目里引用发布的 Jar 包   
### a、在 gradle.build 文件中的 repositories 加入
```
maven {url https://raw.githubusercontent.com/username/maven-repo/master}
```
### b、并在 dependencies 加入
```
compile 'io.github.username.jlib:util:0.1'
```
   
---
[如何发布jar/aar到本地仓库](https://www.jianshu.com/p/0629548ab5a4 "如何发布jar/aar到本地仓库")