# 安裝python的grpc
1. 開啟一個虛擬環境
2. 使用pip安裝grpcio==1.19.0
3. pip install grpcio-tools==1.19.0

# 編譯一個協定溝通用的proto檔案
1. 詳細的定義參照: https://reurl.cc/nv541
2. 根據官網的範例定義helloworld.proto
```
syntax = "proto3";

option java_multiple_files = true;
option java_package = "io.grpc.examples.helloworld";
option java_outer_classname = "HelloWorldProto";
option objc_class_prefix = "HLW";

package helloworld;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}

```

# 使用grpc_tools.protoc產生code
> python -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./helloworld.proto


# reference
1. https://grpc.io/docs/quickstart/python.html
2. https://grpc.io/docs/tutorials/basic/python.html
3. https://github.com/grpc/grpc/tree/v1.19.0/examples/python