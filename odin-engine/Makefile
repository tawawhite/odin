GO_CMD=go
GO_BUILD=$(GO_CMD) build
GO_CLEAN=$(GO_CMD) clean
GO_TEST=$(GO_CMD) test
GO_GET=$(GO_CMD) get
NAME=odin-engine
DIR=./cmd/odin-engine

all: test build
build:
	$(GO_BUILD) -o $(NAME) -v $(DIR)
install:
	$(GO_BUILD) -o /bin/$(NAME) -v $(DIR)
test:
	$(GO_TEST) -v -cover ./...
clean:
	$(GO_CLEAN) -v ./...
	rm -f $(NAME)
	rm -r ./pkg/jobs/here
	rm -r ./pkg/jobs/now
run:
	./$(NAME)
