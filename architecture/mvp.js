// IView接口
class IView {
  render(data) {}
  setPresenter(presenter) {}
}

// 具体的View实现，不与Model直接交互
class View extends IView {
  constructor() {
    super();
    this.presenter = null;
  }

  setPresenter(presenter) {
    this.presenter = presenter;
  }

  // 用户操作，通知Presenter
  onUserAction() {
    this.presenter.handleUserAction();
  }

  // Presenter通知View更新
  render(data) {
    console.log(`视图显示数据：${data}`);
  }
}

// Model，不与View直接交互
class Model {
  constructor() {
    this.data = "初始数据";
    this.listeners = [];
  }

  getData() {
    return this.data;
  }

  setData(newData) {
    this.data = newData;
    this.notifyListeners();
  }

  // 添加监听器
  addListener(listener) {
    this.listeners.push(listener);
  }

  // 通知监听器
  notifyListeners() {
    this.listeners.forEach((listener) => listener());
  }
}

// Presenter，依赖于IView接口
class Presenter {
  constructor(model, view) {
    this.model = model;
    this.view = view;

    // Presenter持有View的引用，并设置自己为View的Presenter
    this.view.setPresenter(this);

    // Presenter监听Model的数据变化
    this.model.addListener(this.onModelChanged.bind(this));
  }

  // 处理来自View的用户操作
  handleUserAction() {
    // 更新Model的数据
    this.model.setData("更新后的数据");
  }

  // 当Model的数据发生变化时，通知View更新
  onModelChanged() {
    const data = this.model.getData();
    this.view.render(data);
  }
}

// 使用示例
const model = new Model();
const view = new View();
const presenter = new Presenter(model, view);

// 模拟用户在View上的操作
view.onUserAction();
