#### 這邊會紀錄一些我使用tensorflow上的筆記
- Q1. tf.Variable 與 tf.constant 的差異
https://stackoverflow.com/questions/44745855/tensorflow-variables-and-constants

```
In TensorFlow the differences between constants and variables are that when you declare some constant,
it's value can't be changed in the future (also the initialization should be with a value, not with operation).

Nevertheless, when you declare a Variable, you can change it value at the future with tf.assign() method
(and the initialization can be with a value or operation).

The function tf.global_variables_initializer() initialises all variables in your code with the value passed as parameter,
but it works in async mode, so don't works propertly when exists dependencies between variables.
```

> 使用tf.constant()宣告出來的變數無法在未來用tf.assign()改變其值。使用tf.Varaible()必須要在使用前先呼叫tf.global_variables_initializer()