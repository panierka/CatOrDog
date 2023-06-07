<template>
    <h1>Kot czy Pies?</h1>

    <div class="image-classification well">
        <FileUploader @change-classification="onClassification"/>
        <h4>
            <p v-if="classificationLabel !== null">
                Twoje zwierzę to {{ classificationLabel }}
            </p>
            <p v-else>
                ???
            </p>

            <p v-if="classificationConfidence !== null">
                Pewność: {{ classificationConfidence }}%
            </p>
        </h4>
    </div>
</template>

<script lang="ts">
import { ClassificationResult } from '../models/ClassificationResult';
import FileUploader from './FileUploader.vue';
import { Component, Vue } from 'vue-facing-decorator';

@Component({
    components: {
        FileUploader
    }
})
export default class CatOrDog extends Vue {
    classificationLabel: string | null = null; 
    classificationConfidence: number | null = null;   

    onClassification(result: ClassificationResult | null){
        if (result === null){
            this.classificationLabel = null;
            this.classificationConfidence = null;
            return;
        }

        const outputsMap: { [id: string] : string; } = {
            'cat': 'kot',
            'dog': 'pies'
        }

        this.classificationLabel = outputsMap[result.cls];
        this.classificationConfidence = result.confidence;
    }
}
</script>