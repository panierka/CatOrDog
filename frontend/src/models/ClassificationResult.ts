export class ClassificationResult {
    cls: string 
    confidence: number

    constructor(cls: string, confidence: number){
        this.cls = cls;
        this.confidence = confidence;
    }
}