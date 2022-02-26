import AbstactView from "./AbstactView.js";

export default class extends AbstactView {
    constructor(params) {
        super(params);
    }

    async getHtml() {
        return `
            <form action="" method="POST">
                <button type="submit">Test</button>
            </form>
        `;
    }
}