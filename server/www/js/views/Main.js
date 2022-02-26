import AbstactView from "./AbstactView.js";

export default class extends AbstactView {
    constructor(params) {
        super(params);
        this.setTitle("Settings");
    }

    async getHtml() {
        return `
            <h1>Home Page!!</h1>
        `;
    }
}