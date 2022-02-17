# ppbot

config.jsonになんかしら入れたら、その通りスラッシュコマンドを作ってくれるはずです。

`config.json` を作成し、以下のように編集してください

```
{
  section:{ <-適当に名前つけてください
    name:name, <- 名前です
    description:description, <- 説明です
    contents:contents <- コマンド打ったら出るやつです
  },
  section2:{ <-適当に名前つけてください
    name:name2, <- 名前です
    description:description2, <- 説明です
    contents:contents2 <- コマンド打ったら出るやつです
  } 
}
```
